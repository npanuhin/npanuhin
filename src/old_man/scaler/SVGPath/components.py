from itertools import islice
from enum import Enum

from .utils import batched, minify_arg, number_to_str


class CONTROL_TYPE(Enum):
    ABSOLUTE = 'A'
    RELATIVE = 'R'


class Command:
    def __init__(self, args, relative=False):
        self.type = CONTROL_TYPE.RELATIVE if relative else CONTROL_TYPE.ABSOLUTE
        self.args = args

    def __str__(self):
        return self.CONTROL_CHARACTERS[self.type] + ','.join(map(number_to_str, self.args))

    def __repr__(self):
        typename = self.__class__.__name__
        _type = 'by ' if self.type == CONTROL_TYPE.RELATIVE else ''
        args = ' | '.join(
            ', '.join(f'{_type}{number_to_str(arg)}' for arg in arg_batch)
            for arg_batch in batched(self.args, self.ARGC)
        ) if self.ARGC else ''
        return f'{typename}({args})'

    def minify(self):
        return ''.join((
            self.CONTROL_CHARACTERS[self.type],
            minify_arg(self.args[0], True) if self.ARGC else '',
            ''.join(map(minify_arg, islice(self.args, 1, None)))
        ))

    def round(self, precision=0):
        for i, arg in enumerate(self.args):
            self.args[i] = round(arg, precision)

    def scale_by(self, coefficient: float):
        for i, arg in enumerate(self.args):
            self.args[i] = arg * coefficient

    def strip_less(self, threshold: float, absolute=False):
        for i, arg in enumerate(self.args):
            if absolute:
                arg = abs(arg)
            if arg <= threshold:
                self.args[i] = 0


class MoveTo(Command):
    ARGC = 2
    CONTROL_CHARACTERS = {
        CONTROL_TYPE.ABSOLUTE: 'M',
        CONTROL_TYPE.RELATIVE: 'm'
    }

    def __init__(self, args, relative=False):
        super().__init__(args, relative)


class ClosePath(Command):
    ARGC = 0
    CONTROL_CHARACTERS = {
        CONTROL_TYPE.ABSOLUTE: 'Z',
        CONTROL_TYPE.RELATIVE: 'z'
    }

    def __init__(self, args, relative=False):
        super().__init__(args, relative)


class LineTo(Command):
    ARGC = 2
    CONTROL_CHARACTERS = {
        CONTROL_TYPE.ABSOLUTE: 'L',
        CONTROL_TYPE.RELATIVE: 'l'
    }

    def __init__(self, args, relative=False):
        super().__init__(args, relative)


class HorizontalLineTo(Command):
    ARGC = 1
    CONTROL_CHARACTERS = {
        CONTROL_TYPE.ABSOLUTE: 'H',
        CONTROL_TYPE.RELATIVE: 'h'
    }

    def __init__(self, args, relative=False):
        super().__init__(args, relative)


class VerticalLineTo(Command):
    ARGC = 1
    CONTROL_CHARACTERS = {
        CONTROL_TYPE.ABSOLUTE: 'V',
        CONTROL_TYPE.RELATIVE: 'v'
    }

    def __init__(self, args, relative=False):
        super().__init__(args, relative)


COMMANDS_BY_CHARACTER = {
    command.CONTROL_CHARACTERS[control_type]: command
    for command in (MoveTo, ClosePath, LineTo, HorizontalLineTo, VerticalLineTo)
    for control_type in CONTROL_TYPE
}

from .components import COMMANDS_BY_CHARACTER
from decimal import Decimal


class SVGPath:
    def __init__(self, d: str = ''):
        self.d = self.components = self._parse_path(d)

    @staticmethod
    def _parse_path(path: str) -> list:
        components = []

        def add_component():
            if not token_stack:
                return

            command, args = token_stack[0], token_stack[1:]
            for i, arg in enumerate(args):
                new_arg = Decimal(arg)
                if '.' not in arg and int(new_arg) == new_arg:
                    new_arg = int(new_arg)
                args[i] = new_arg
            components.append(COMMANDS_BY_CHARACTER[command](args, relative=command.islower()))

        pos = 0
        token_stack = []
        cur_token = []
        while pos < len(path):
            char = path[pos]

            if char in COMMANDS_BY_CHARACTER or char.isspace() or char in '+-,' or (char == '.' and '.' in cur_token):
                if cur_token:
                    token_stack.append(''.join(cur_token))
                    cur_token = []

            if char.isspace():
                pass

            elif char == ',':
                assert token_stack and token_stack[-1] not in COMMANDS_BY_CHARACTER, \
                    f'Unexpected comma at position {pos}'

            elif char.isdecimal() or char in '+-.':
                cur_token.append(char)

            elif char in COMMANDS_BY_CHARACTER:
                add_component()
                token_stack = [char]

            else:
                raise ValueError(f'Unexpected character "{char}"')

            pos += 1

        if cur_token:
            token_stack.append(''.join(cur_token))
        add_component()
        return components

    def __repr__(self):
        return f'SVGPath({self.components})'

    def __str__(self):
        return ''.join(str(component) for component in self.components)

    def minify(self):
        return ''.join(component.minify() for component in self.components)

    def round(self, precision=0):
        for component in self.components:
            component.round(precision)

    def scale_by(self, coefficient: float):
        for component in self.components:
            component.scale_by(coefficient)

    def strip_less(self, threshold: float, absolute=False):
        for component in self.components:
            component.strip_less(threshold, absolute)


if __name__ == '__main__':
    # test_path = SVGPath('M 1 , 2 m 3  4 Z z')
    # test_path = SVGPath('M1,2,3,4,5,6,7,8,9,10m3,4h-8H-0.2Zz')
    # test_path = SVGPath("h-8.95703125")

    test_path = 'm1436.1721191406,108.504699707v-22.1028442383h-10.9565429688v16.0747680664h-4.9663085938v-10.0466918945h-8.95703125v-10.0467529297h-14.927734375v-5.0233764648h-15.9326171875v5.0233764648h-4.9760742188v16.0747680664h-9.9521484375v28.130859375h8.95703125v6.0280151367h5.9711914062v4.0186767578h-34.83203125v9.0420532227h-8.9565429688'  # noqa
    assert SVGPath(test_path).minify() == test_path

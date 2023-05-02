from itertools import islice
from decimal import Decimal


def batched(iterable, n):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def minify_arg(number: float | int, is_first=False) -> str:
    negative = number < 0
    needs_comma = not is_first and not negative

    if isinstance(number, int):
        return (',' if needs_comma else '') + number_to_str(number)

    if negative:
        string = number_to_str(abs(number))
    else:
        string = number_to_str(number)

    if '.' in string:
        string = string.lstrip('0')
        if string[0] == '.':
            needs_comma = False

    return (',' if needs_comma else '') + ('-' if negative else '') + string


def decimal_to_str(number: Decimal) -> str:
    p = abs(number.as_tuple().exponent)
    return ('{:.%df}' % p).format(number)


def number_to_str(number: int | float | Decimal) -> str:
    if isinstance(number, Decimal):
        return decimal_to_str(number)

    return str(number)

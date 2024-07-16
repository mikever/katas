# pylint: disable=redefined-builtin
# pylint: disable=missing-function-docstring

""" Unique in order

Implement the function 'unique_in_order' which takes as argument a sequence and returns a list
of items without any elements with the same value next to each other and preserving the original
order of elements.
"""


def unique_in_order(sequence):
    """
    Uses list comprehension to always have first item and any item that is not the same
    as the item before it
    """
    return [
        sequence[i]
        for i in range(len(sequence))
        if i == 0 or sequence[i] != sequence[i - 1]
    ]


def unique_in_order_2(iterable):
    """
    Initially sets `prev` to `None` and then appends if current character is not the same as `prev`
    """
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

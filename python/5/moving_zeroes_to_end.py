# pylint: disable=expression-not-assigned
""" Moving Zeroes to the End

Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
"""


def move_zeros(lst):
    """
    Simple but inelegant approach using list comprehensions. We iterate three times.
    """
    zeroes = [x for x in lst if x == 0]
    no_zeroes = [x for x in lst if x != 0]
    [no_zeroes.append(x) for x in zeroes]
    return no_zeroes


def move_zeros2(lst):
    """
    One iteration through the list, removing and appending where needed.
    """
    for i in lst:
        if i == 0:
            lst.remove(i)  # remove element from array
            lst.append(i)  # append element to the end
    return lst

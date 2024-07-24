""" Find the Parity Outlier

You are given an array (which will have a length of at least 3, but could be very large) containing
integers. The array is either entirely comprised of odd integers or entirely comprised of even
integers except for a single integer N. Write a method that takes the array as an argument and
returns this "outlier" N.

Examples:
    [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

    [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

"""


def find_outlier(integers):
    """
    Tests first three items to discover if outlier is even or odd,
    then iterates list to find the outlier. But this solution
    iterates the first three items again unecessarily, and also has
    a `return None` at the end that is not elegant.
    """
    outlier = False
    first_item = (integers[0] % 2) == 0
    second_item = (integers[1] % 2) == 0
    third_item = (integers[2] % 2) == 0

    if first_item == second_item:
        outlier = not first_item
    elif first_item == third_item:
        outlier = second_item
    elif second_item == third_item:
        outlier = first_item

    # once flag is known, iterate the array looking for the outlier
    for i in integers:
        if (i % 2 == 0) == outlier:
            return i

    return None


def find_outlier2(integers):
    """
    Clever. This does iterate the list twice, but so does the solution above.
    """
    odds = [x for x in integers if x % 2 != 0]
    evens = [x for x in integers if x % 2 == 0]

    return odds[0] if len(odds) < len(evens) else evens[0]

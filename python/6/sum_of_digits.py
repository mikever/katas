""" Sum of Digits / Digital Root

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.

    Examples
        16  -->  1 + 6 = 7
       942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
    132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
    493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""


def digital_root(n):
    """
    Recursion
    """
    sum_num = 0

    for digit in str(n):
        sum_num += int(digit)
    if len(str(sum_num)) > 1:
        sum_num = digital_root(sum_num)
    return sum_num


def digital_root2(n):
    """
    Clever conditional on `n < 10`, as well as the use of a `sum()` on a `map()`.
    """

    return n if n < 10 else digital_root2(sum(map(int, str(n))))

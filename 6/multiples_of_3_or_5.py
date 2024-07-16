# pylint: disable=redefined-builtin
""" Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5
below the number passed in.
Additionally, if the number is negative, return 0.
Note: If the number is a multiple of both 3 and 5, only count it once.
"""


# My initial solution
def solution(number):
    """This could be done better with a list comprehension"""
    if number < 0:
        return 0

    list = []

    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            list.append(num)

    return sum(list)


def solution_2(number):
    """A one-liner that uses a generator comprehension"""
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


def solution_3(number):
    """
    Adding to sum as we iterate over the list.
    This might be the a more readable solution than solution_2
    """
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum

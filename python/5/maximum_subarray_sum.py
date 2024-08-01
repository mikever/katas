""" Maximum Subarray Sum
The maximum sum subarray problem consists in finding the maximum sum of a contiguous
subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the
sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array
is also a valid sublist/subarray.
"""


def max_sequence(arr):
    """
    Keepign track of max_so_far, and increasing it based on max_ending_here while iterating array
    """
    if len(arr) == 0:
        return 0

    size = len(arr)
    max_so_far = arr[0]
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here += arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max(max_so_far, 0)


def max_sequence2(arr):
    """
    An elegant approach, with terse but precise `if` statement syntax and style
    Also note the single-line `num = max(num, 0)` instead of an `if` statement
    """
    maximum, curr = 0, 0
    for x in arr:
        curr += x
        curr = max(curr, 0)
        maximum = max(maximum, 0)
    return maximum

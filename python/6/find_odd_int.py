""" Find The Odd Int

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples:
    [7] should return 7, because it occurs 1 time (which is odd).
    [0] should return 0, because it occurs 1 time (which is odd).
    [1,1,2] should return 2, because it occurs 1 time (which is odd).
    [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
    [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""

from typing import Optional


def find_it(seq: list[int]) -> Optional[int]:
    """Build a hash table and then iterate it to find odd number; Not efficient"""
    cache = {}
    for x in seq:
        if cache.get(x, 0):
            cache[x] = cache[x] + 1
        else:
            cache[x] = 1
    for k, v in cache.items():
        if v % 2 != 0:
            return k
        return None


def find_it_2(seq: list[int]) -> Optional[int]:
    """More efficient
    Count number of entried as we iterate the list
    Allows us to short circuit iteration of list as soon as we find odd entry
    """
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
        return None

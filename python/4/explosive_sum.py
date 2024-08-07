""" Explosive Sum
How many ways can you make the sum of a number?

> From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)
> 
> In number theory and combinatorics, a partition of a positive integer n,
> also called an integer partition, is a way of writing n as a sum of positive
> integers. Two sums that differ only in the order of their summands are
> considered the same partition. If order matters, the sum becomes a composition.
> For example, 4 can be partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1

Examples:
    Basic
    exp_sum(1) # 1
    exp_sum(2) # 2  -> 1+1 , 2
    exp_sum(3) # 3 -> 1+1+1, 1+2, 3
    exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
    exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

    exp_sum(10) # 42
    Explosive
    exp_sum(50) # 204226
    exp_sum(80) # 15796476
    exp_sum(100) # 190569292
"""


def exp_sum(n):
    """Perhaps not the most efficient for large numbers"""
    if n < 0:
        return 0
    partitions = [1] + [0] * n
    for num in range(1, n + 1):
        for i in range(num, n + 1):
            partitions[i] += partitions[i - num]
    return partitions[-1]


# -----


class Memoize:
    """
    Creates a cache and use recursion in the __call__
    """

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, arg):
        if arg not in self.cache:
            self.cache[arg] = self.func(arg)
        return self.cache[arg]


@Memoize
def exp_sum_2(n):
    """Not sure what's happening here"""
    if n == 0:
        return 1
    result = 0
    k = 1
    sign = 1
    while True:
        pent = (3 * k**2 - k) // 2
        if pent > n:
            break
        result += sign * exp_sum(n - pent)
        pent += k
        if pent > n:
            break
        result += sign * exp_sum(n - pent)
        k += 1
        sign = -sign
    return result

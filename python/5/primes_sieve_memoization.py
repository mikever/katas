""" Master Your Primes: Sieve With Memoization

As most of you might know already, a prime number is an integer n with the following properties:

it must be greater than 1
it must be divisible only by itself and 1
And that's it: -15 or 8 are not primes, 5 or 97 are; pretty easy, isn't it?

Well, turns out that primes are not just a mere mathematical curiosity and are very important,
for example, to allow a lot of cryptographic algorithms.

Being able to tell if a number is a prime or not is thus not such a trivial matter and doing
it with some efficient algo is thus crucial.

There are already more or less efficient (or sloppy) katas asking you to find primes, but here
I try to be even more zealous than other authors.

You will be given a preset array/list with the first few primes. And you must write a function
that checks if a given number n is a prime looping through it and, possibly, expanding the
array/list of known primes only if/when necessary (ie: as soon as you check for a potential
prime which is greater than a given threshold for each n, stop).

Memoization:
Storing precomputed results for later re-use is a very popular programming technique that you
would better master soon and that is called memoization; while you have your wiki open, you might
also wish to get some info about the sieve of Eratosthenes (one of the few good things I learnt
as extra-curricular activity in middle grade) and, to be even more efficient, you might wish to
consider an interesting reading on searching from prime from a friend of mine [she thought about
an explanation all on her own after an evening event in which I discussed primality tests with
my guys].

Yes, you will be checked even on that part. And you better be very efficient in your code if you
hope to pass all the tests ;)

Dedicated to my trainees that worked hard to improve their skills even on a holiday: good work guys!

Or should I say "girls" ;)? Agata, Ania Dina and (although definitely not one of my trainees)
special mention to NaN
"""

# pylint: disable=global-variable-not-assigned

primes = [2, 3, 5, 7]
primes_set = set(primes)


def is_prime(n):
    """Uses memoization"""
    global primes_set

    if n <= primes[-1]:
        return n > 1 and n in primes_set
    limit = int(n**0.5)
    for x in primes:
        if x > limit:
            break
        if not n % x:
            return False

    x, delta = primes[-1], 4 if primes[-1] % 6 == 1 else 2
    while x <= limit:
        x, delta = x + delta, 6 - delta
        if is_prime(x):
            primes.append(x)
            primes_set.add(x)
            if not n % x:
                return False
    return True

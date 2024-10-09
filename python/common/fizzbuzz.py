""" FizzBuzz

Take in a number. Iterate from 1 to the number, and return 'Fizz' if the number is divisible by 3,
return 'Buzz' if the number is divisible by 5, and return 'FizzBuzz' if the number is divisible
by 15.
"""


def fizz_buzz(n):
    for fb in range(n):
        fb = fb + 1
        if fb % 15 == 0:
            print("fizzbuzz")
            continue
        if fb % 5 == 0:
            print("buzz")
            continue
        if fb % 3 == 0:
            print("fizz")
            continue
        print(str(fb))


fizz_buzz(50)

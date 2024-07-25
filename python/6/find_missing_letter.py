""" Find the Missing Letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:
    ['a','b','c','d','f'] -> 'e'
    ['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)
"""


def find_missing_letter(chars):
    """
    Uses `ord` function to convert to numerical representation
    """
    last_value = ord(chars[0])
    missing_letter = ""
    for i in chars:
        current_value = ord(i)
        if current_value in (last_value, last_value + 1):
            last_value = current_value
        else:
            return chr(ord(i) - 1)
    return missing_letter


def find_missing_letter2(chars):
    """
    A simplified approach
    """
    n = 0
    while ord(chars[n]) == ord(chars[n + 1]) - 1:
        n += 1
    return chr(1 + ord(chars[n]))

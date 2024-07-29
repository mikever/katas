""" Simple Pig Latin

Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples:
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    """
    inelegant: not using `isalpha` and not using a single list comprehension
    """
    words = text.split()
    pigified = [word[1:] + word[0] + "ay" for word in words]
    corrected = []
    for word in pigified:
        if word in [".ay", "!ay", "?ay", ",ay"]:
            corrected.append(word[0])
        else:
            corrected.append(word)

    return " ".join(corrected)


def pig_it2(text):
    """
    uses `isalpha()` function with an `else` in the list comprehension
    """
    words = text.split()
    return " ".join(
        [word[1:] + word[:1] + "ay" if word.isalpha() else word for word in words]
    )

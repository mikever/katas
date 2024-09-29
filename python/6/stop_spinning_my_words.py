""" Stop Spinning My Words

Write a function that takes in a string of one or more words, and returns the same string,
but with all words that have five or more letters reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces. Spaces will be included only when
more than one word is present.

Examples:
    "Hey fellow warriors"  --> "Hey wollef sroirraw" 
    "This is a test        --> "This is a test" 
    "This is another test" --> "This is rehtona test"
"""


def spin_words(sentence: str) -> str:
    """Uses an if-else in a list comprehension"""
    words = sentence.split()
    corrected = [x if len(x) < 5 else x[::-1] for x in words]
    return " ".join(corrected)


def spin_words2(sentence: str) -> str:
    """One-line solution"""
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


print(spin_words("Stop Spinning my Words"))
print(spin_words2("Stop Spinning my Words"))

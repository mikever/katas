""" Roman Numerals Helper

Write two functions that convert a roman numeral to and from an integer value.
Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting
with the left most digit and skipping any digit with a value of zero. In Roman numerals:

1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
2008 is written as 2000=MM, 8=VIII; or MMVIII
1666 uses each Roman symbol in descending order: MDCLXVI.
Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples:
    To roman:
    2000 -> "MM"
    1666 -> "MDCLXVI"
      86 -> "LXXXVI"
       1 -> "I"

    From roman:
    "MM"      -> 2000
    "MDCLXVI" -> 1666
    "LXXXVI"  ->   86
    "I"       ->    1
"""


class RomanNumerals:
    """
    Methods
    -------
    to_roman(int):
        converts decimal int to Roman numeral string

    from_roman(str):
        converts Roman numeral string to decimal int
    """

    @staticmethod
    def to_roman(val: int) -> str:
        """lists of strings for decimal place; floor division; concat result string"""
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        thousands = m[val // 1000]
        hundreds = c[(val % 1000) // 100]
        tens = x[(val % 100) // 10]
        ones = i[val % 10]

        return thousands + hundreds + tens + ones

    @staticmethod
    def from_roman(roman_num: str) -> int:
        """Iterate, jump by two or one, depending on the numeral on the dict; add to number depending on value of letter"""
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        i = 0
        num = 0
        str_length = len(roman_num)
        while i < str_length:
            if i + 1 < str_length and roman_num[i : i + 2] in roman:
                num += roman[roman_num[i : i + 2]]
                i += 2
            else:
                num += roman[roman_num[i]]
                i += 1
        return num

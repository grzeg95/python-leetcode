# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:

        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_letter: None | str = None

        for letter in s:

            if prev_letter is not None and symbols[prev_letter] < symbols[letter]:
                total -= symbols[prev_letter]
                total += symbols[letter] - symbols[prev_letter]

            if prev_letter is not None and symbols[prev_letter] >= symbols[letter]:
                total += symbols[letter]

            if prev_letter is None:
                total += symbols[letter]

            prev_letter = letter

        return total

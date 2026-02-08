# https://leetcode.com/problems/palindrome-number/

import math

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        if x < 10:
            return True

        # https://mathworld.wolfram.com/NumberLength.html
        x_len = int(math.log(x, 10)) + 1

        while x_len > 1:

            right = x % 10
            left = int(x / 10 ** (x_len - 1))

            if right != left:
                return False

            x -= 10 ** (x_len - 1) * left
            x = int(x / 10)
            x_len -= 2

        return True

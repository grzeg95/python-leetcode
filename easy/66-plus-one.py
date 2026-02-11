# https://leetcode.com/problems/plus-one/

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits) - 1
        res = []

        total = digits[i] + 1
        last_digit = total % 10
        carriage = total // 10
        res.append(last_digit)
        i -= 1

        while i >= 0:
            total = digits[i] + carriage
            last_digit = total % 10
            carriage = total // 10
            res.append(last_digit)
            i -= 1

        if carriage > 0:
            res.append(carriage)

        return list(reversed(res))

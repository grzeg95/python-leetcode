# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        precision = 10 ** (-1)

        while abs(x - r * r) > precision:
            r = (r + x / r) / 2

        return int(r)
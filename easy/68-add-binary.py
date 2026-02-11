# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        ai = len(a) - 1
        bi = len(b) - 1
        result = ''

        carriage = 0

        while ai >= 0 or bi >= 0:

            if ai >= 0:
                ax = int(a[ai])
                ai -= 1
            else:
                ax = 0

            if bi >= 0:
                bx = int(b[bi])
                bi -= 1
            else:
                bx = 0

            total = ax + bx + carriage
            last_digit = total % 2
            carriage = total // 2
            result += str(last_digit)

        if carriage > 0:
            result += str(carriage)

        return result[::-1]
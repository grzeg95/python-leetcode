# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        i = len(s) - 1
        length = 0

        while s[i] == ' ':
            i -= 1

        while s[i] != ' ' and i >= 0:
            length += 1
            i -= 1

        return length

# https://leetcode.com/problems/valid-parentheses/

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:

        brackets: List[str] = []

        for bracket in s:

            if bracket in ['(', '{', '[']:
                brackets.append(bracket)
                continue

            if len(brackets) == 0:
                return False

            prev_bracket = brackets.pop()

            if (
                prev_bracket == '(' and bracket != ')' or
                prev_bracket == '{' and bracket != '}' or
                prev_bracket == '[' and bracket != ']'
            ):
                return False

        return len(brackets) == 0

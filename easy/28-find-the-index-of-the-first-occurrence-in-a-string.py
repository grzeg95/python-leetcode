# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1

        i = 0

        while i < len(haystack):

            if haystack[i] == needle[0]:
                if len(haystack) - i < len(needle):
                    return -1
                else:
                    j = 0
                    start = i
                    while True:

                        if haystack[i] == needle[j]:
                            i += 1
                            j += 1
                        else:
                            break

                        if j == len(needle) or i == len(haystack):
                            break

                    if j == len(needle):
                        return start
                    else:
                        i = start

            i += 1

        return -1

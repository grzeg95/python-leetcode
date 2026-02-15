# https://leetcode.com/problems/merge-sorted-array/description/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = (m + n) - 1
        ax = m - 1
        bx = n - 1

        while ax >= 0 and bx >= 0:

            if nums1[ax] > nums2[bx]:
                nums1[i] = nums1[ax]
                i -= 1
                ax -= 1
            else:
                nums1[i] = nums2[bx]
                i -= 1
                bx -= 1

        if ax < 0:
            while bx >= 0:
                nums1[i] = nums2[bx]
                i -= 1
                bx -= 1

        if bx < 0:
            while ax >= 0:
                nums1[i] = nums1[ax]
                i -= 1
                ax -= 1

        return nums1

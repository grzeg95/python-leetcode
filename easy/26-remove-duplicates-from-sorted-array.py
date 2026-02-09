# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left + 1] = nums[right]
                left += 1
                right += 1

        return left + 1

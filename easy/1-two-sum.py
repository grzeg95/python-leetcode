# https://leetcode.com/problems/two-sum/

from typing import List, Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        differences: Dict[int, int] = {}
        result: List[int] = []

        for index, num in enumerate(nums):
            if num in differences:
                result = [index, differences[num]]
                break
            differences[target - num] = index

        return result

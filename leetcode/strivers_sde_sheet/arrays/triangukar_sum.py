from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for _ in range(len(nums)):
            temp = list()
            for j in range(len(nums) - 1):
                temp.append(nums[j]+ nums[j+1])

            nums = temp
        
        if nums and len(nums) == 1:
            return nums[0]
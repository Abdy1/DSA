# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if self.isSorted(nums):
            return True
        
        for i in range(len(nums)):
            if nums[i] > nums[i+1]:
                curr = nums[i]
                nums[i] = nums[i+1]
                left = self.isSorted(nums)
                nums[i], nums[i+1] = curr,curr
                right = self.isSorted(nums)
                return left or right
        return True

    def isSorted(self, nums: List[int]) -> bool:
        sorted_num = sorted(nums)
        return sorted_num == nums
        
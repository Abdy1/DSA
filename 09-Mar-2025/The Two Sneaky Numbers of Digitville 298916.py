# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # go through list and starting from where i am look for item if so add to ans
        ans = []
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                ans.append(nums[i])
        return ans

        
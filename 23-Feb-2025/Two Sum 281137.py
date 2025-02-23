# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementary = {}
        for idx, item in enumerate(nums):
            diff = target - item
            if diff in complementary:
                return [complementary[diff],idx]
            complementary[item] = idx


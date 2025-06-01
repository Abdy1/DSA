# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow , fast = 0, 0
        n = len(nums)
        total = 0
        minimum = float("inf")

        for fast in range(n):
            total += nums[fast]
            while total >= target: 
                minimum = min(minimum, (fast-slow) + 1)
                total -= nums[slow]
                slow += 1
    

        return 0 if minimum == float("inf") else minimum



                



        
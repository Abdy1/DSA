# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum

        l = 0
        r = k
        while r < len(nums):
            current_sum += nums[r] - nums[l]
            max_sum = max(max_sum,current_sum)
            l += 1
            r += 1
        return max_sum/k
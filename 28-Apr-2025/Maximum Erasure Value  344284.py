# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        summ = 0
        window = set()
        window.add(summ)
        ans = 0
        for r in range(len(nums)):
            while nums[r] in window:
                window.remove(nums[l])
                summ -= nums[l]
                l += 1
            window.add(nums[r])
            summ += nums[r]
            ans = max(ans, summ)
        return ans




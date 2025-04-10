# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        remaining = sum(nums) - x
        summ = 0
        left = 0
        maxx = -1
        for right in range(len(nums)):
            summ += nums[right]
            print(left, right)
            while summ > remaining and left <= right:
                summ -=nums[left]
                left +=1
            if summ == remaining:
                maxx = max(maxx, right-left+1)

        return len(nums)-maxx if maxx != -1 else -1

        
# Problem: Patching Array - https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        x = 1
        patches = 0
        i = 0
        while x <= n:
            if i < len(nums) and nums[i] <= x:
                x += nums[i]
                i += 1
            else:
                patches += 1
                x *= 2
        return patches

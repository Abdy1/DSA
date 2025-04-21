# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        ans = 0
        nums.sort()
        while left < right:
            summ = nums[left] + nums[right]
            if summ < target:
                ans += (right - left)
                left += 1
            else:
                right -= 1
        return ans
               

        
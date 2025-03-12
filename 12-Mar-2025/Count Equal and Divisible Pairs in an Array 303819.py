# Problem: Count Equal and Divisible Pairs in an Array - https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # prepare count 
        count = 0

        # loop through the nums
        # for each item looop through all elements on the right
        # at each iteration first check if their value is equal if so multiply them and devide them by k and check if remainder is zero. if so increment count
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i*j)%k==0:
                    count += 1
        return count
        
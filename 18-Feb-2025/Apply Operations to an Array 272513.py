# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if i != len(nums)-1:
                if nums[i] == nums[i+1]:
                    nums[i] *= 2
                    nums[i+1] = 0

        pop_count = 0
        while 0 in nums:
            nums.remove(0)
            pop_count += 1

        for i in range(pop_count):
            nums.append(0)

        return nums



        
# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        place_holder = 0
        seeker = 1

        for seeker in range(len(nums)):
            if nums[seeker] != 0:
                nums[seeker], nums[place_holder] = nums[place_holder], nums[seeker]
                place_holder += 1
            


        
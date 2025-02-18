# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        nums = [i for i in range(1,n+1)]
        count_down = k

        index = 0
        while len(nums) != 1:
            count_down -= 1
            if count_down == 0:
                nums.pop(index)
                count_down = k
            else:
                index = (index + 1) % len(nums)
        return nums[0]
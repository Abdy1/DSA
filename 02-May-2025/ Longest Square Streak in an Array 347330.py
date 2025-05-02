# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        sett = set(nums)
        visited = set()
        max_len = -1

        for num in sett:
            if num in visited:
                continue
            current = num
            length = 0
            while current in sett:
                visited.add(current)
                current = current * current
                length += 1
            if length >= 2:
                max_len = max(max_len, length)
        
        return max_len

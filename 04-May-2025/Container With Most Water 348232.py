# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l  = 0
        r = len(height) -1 
        max_area = 0
        while l < r:
            if height[l] > height[r]:
                area = height[r] * (r-l)
                r -= 1
            else:
                area = height[l] * (r-l)
                l += 1
            max_area = max(max_area, area)
        return max_area


        
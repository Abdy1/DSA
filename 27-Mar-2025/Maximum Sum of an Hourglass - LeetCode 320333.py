# Problem: Maximum Sum of an Hourglass - LeetCode - https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)  
        n = len(grid[0]) 
        
        if m < 3 or n < 3:
            return None 
        
        max_sum = float('-inf') 

        for i in range(1, m-1): 
            for j in range(1, n-1):  
                top = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
                middle = grid[i][j]
                bottom = grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
                hourglass_sum = top + middle + bottom
                
                max_sum = max(max_sum, hourglass_sum)
        
        return max_sum
            
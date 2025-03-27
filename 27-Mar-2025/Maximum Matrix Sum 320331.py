# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg = 0
        maxx = 0
        minn = float('inf')
        
        for row in matrix:
            for cell in row:
                maxx += abs(cell)
                minn = min(minn, abs(cell))
                if cell < 0:
                    neg += 1
        if neg & 1:
            maxx -= 2 * minn
        return maxx 
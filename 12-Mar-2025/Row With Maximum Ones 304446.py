# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        
        index = 0
        count = 0
        for i in range(m):
            if mat[i].count(1) > count:
                count = mat[i].count(1)
                index = i
        return [index,count]

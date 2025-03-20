# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up = True
        res = []
        i = 0
        j = 0
        while i < len(mat) and j < len(mat[0]):
                res.append(mat[i][j])
                if up:
                    if i - 1 >= 0 and j + 1 < len(mat[0]):
                        i -= 1
                        j += 1
                    else:
                        if j + 1 < len(mat[0]):
                            j += 1
                        else:
                            i += 1
                        up = not up
                else:
                    if i+1 < len(mat) and j -1 >= 0:
                        i += 1
                        j -= 1
                    else:
                        if i + 1 < len(mat):
                            i += 1
                        else:
                            j += 1
                        up = not up
                       
        return res
        
# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        column = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            row = row[::-1]
            column.append(row)
        for i in range (len(column)):
            matrix[i] = column[i]
            

   

                


        """
        Do not return anything, modify matrix in-place instead.
        """
        
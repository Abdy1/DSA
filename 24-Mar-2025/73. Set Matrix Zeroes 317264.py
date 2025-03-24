# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])

        first_row_0 = False
        first_column_0 = False

        for i in range(columns):
            if matrix[0][i] == 0:
                first_row_0 = True
                break
        
        for i in range(rows):
            if matrix[i][0] == 0:
                first_column_0 = True
                break

        for i in range(1, rows):
            for j in range(1, columns):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,rows):
            for j in range(1, columns):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row_0:
            for i in range(columns):
                matrix[0][i] = 0
        if first_column_0:
            for i in range(rows):
                matrix[i][0] = 0


        
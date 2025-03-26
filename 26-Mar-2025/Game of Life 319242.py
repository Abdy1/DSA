# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        def count_live_neighbors(r, c):
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] in [1, -1]:  
                        live_neighbors += 1
            return live_neighbors
        
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r, c)
                if board[r][c] == 1:
                    # Rule 1 or Rule 2
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1  # Mark as a cell that will die in the next generation
                elif board[r][c] == 0:
                    # Rule 4
                    if live_neighbors == 3:
                        board[r][c] = 2  # Mark as a cell that will become alive in the next generation
        
        # Second pass: Update the board based on the temporary markings
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 0  # Dead in the next generation
                elif board[r][c] == 2:
                    board[r][c] = 1  # Alive in the next generation

# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        
        def dfs(i, j, k):
            # If we found all letters
            if k == len(word):
                return True
            # Check bounds, character match, and whether visited
            if i<0 or i>=m or j<0 or j>=n or visited[i][j] or board[i][j] != word[k]:
                return False
            
            visited[i][j] = True
            # Explore all four directions
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                if dfs(i+di, j+dj, k+1):
                    return True
            
            visited[i][j] = False  # backtrack
            return False
        
        # Try starting from every position
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

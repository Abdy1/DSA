# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if not img or not img[0]:  # Add input validation
            return []
            
        m, n = len(img), len(img[0])
        directions = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0], 
                     [1, 1], [1, -1], [-1, 1], [-1, -1]]
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n:
                        total += img[x][y]
                        count += 1
                result[i][j] = total // count
                
        return result
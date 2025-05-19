# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        img1_ones = [(i,j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        img2_ones = [(i,j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        count = defaultdict(int) 
        for (x1,y1) in img1_ones:
            for (x2, y2) in img2_ones:
                trans = (x1-x2, y1-y2)
                count[trans] += 1
        return max(count.values(), default=0)



            
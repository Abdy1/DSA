# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        for i in range(n):
            print(image[i])
            image[i].reverse()
            for j in range(n):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        return image

        
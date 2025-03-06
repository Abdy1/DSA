# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_height = []
        length = len(names)
        for i in range(length):
            name_height.append([names[i],heights[i]])

        for i in range(length):
            for j in range(i+1,length):
                if name_height[i][1] < name_height[j][1]:
                    name_height[i], name_height[j] = name_height[j], name_height[i]


        return [item[0] for item in name_height]


   
        
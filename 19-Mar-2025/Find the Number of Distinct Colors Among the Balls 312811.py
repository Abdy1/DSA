# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        visit_balls = {}  
        visit_colours = {}  
        count = 0  
        res = []

        for ball, colour in queries:
            if ball not in visit_balls:
                visit_colours[colour] = visit_colours.get(colour, 0) + 1
                visit_balls[ball] = colour
                
                if visit_colours[colour] == 1:
                    count += 1
            
            else:
                old_colour = visit_balls[ball]
                if colour == old_colour:
                    res.append(count)
                    continue

                visit_balls[ball] = colour
                

                visit_colours[old_colour] -= 1
                if visit_colours[old_colour] == 0:
                    del visit_colours[old_colour]
                    count -= 1
   
                visit_colours[colour] = visit_colours.get(colour, 0) + 1
                if visit_colours[colour] == 1:
                    count += 1
                
            res.append(count)

        return res
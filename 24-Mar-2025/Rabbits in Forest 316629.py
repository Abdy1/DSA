# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Step 1: Count the frequency of each answer
        count = Counter(answers)
        
        total_rabbits = 0
        
        # Step 2: Calculate the number of rabbits needed for each answer group
        for x, freq in count.items():
            # For each distinct answer 'x', we need ceil(freq / (x + 1)) groups
            groups_needed = math.ceil(freq / (x + 1))
            total_rabbits += groups_needed * (x + 1)
        
        return total_rabbits
# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
                # Iterate over possible values of a from 0 to √c
        for a in range(int(math.sqrt(c)) + 1):
            b = math.sqrt(c - a*a)
            # Check if b is an integer
            if b.is_integer():
                return True
        return False
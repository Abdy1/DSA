# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n):
            sum_of_squares_var = 0
            while n > 0:
                n, digit = divmod(n,10)
                sum_of_squares_var += digit * digit
            return sum_of_squares_var
       
        seen = set()

        while n != 1 and n not in seen:
           seen.add(n)
           n = sum_of_squares(n)

        return n == 1

  
      




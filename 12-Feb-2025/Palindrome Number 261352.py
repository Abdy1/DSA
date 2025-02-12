# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        rev = []
        while x:
            result, reminder = divmod(x,10)
            rev.append(reminder)
            x = result
        return rev[::-1] == rev

        
# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
    
        for char in s:
            if char.isdigit():  # If it's a digit, try to remove the last non-digit
                if stack:  # There is a character to the left
                    stack.pop()  # Remove the closest non-digit character
            else:
                stack.append(char)  # Otherwise, add the non-digit character to the stack
        
        # The result is the content of the stack joined as a string
        return ''.join(stack)
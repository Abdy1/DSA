# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char) 
            if char == ')':
                if not self.checker(stack, '('):
                    return False     
            if char == '}':
                if not self.checker(stack, '{'):
                    return False    
            if char == ']':
                if not self.checker(stack, '['):
                    return False
        return not stack
    def checker(self, stack, expected):
        if not stack or stack[-1] != expected:
            return False
        else:
            stack.pop()
            return True




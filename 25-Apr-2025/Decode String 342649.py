# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                strr = ''
                while stack[-1] != '[':
                    item = stack.pop()
                    strr = item + strr
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    item = stack.pop()
                    k = item + k
                stack.append(int(k) * strr)
        return ''.join(stack)
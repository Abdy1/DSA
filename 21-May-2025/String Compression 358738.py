# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        stack = []
        count = 1

        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1
            else:
                stack.append(chars[i - 1])
                if count > 1:
                    for c in str(count):
                        stack.append(c)
                count = 1

        # Copy back to chars
        for i in range(len(stack)):
            chars[i] = stack[i]

        return len(stack)

# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_length = 1
        start = 0
        count = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1

            while count > 1:
                if s[start] == s[start + 1]:
                    count -= 1
                start += 1

            max_length = max(max_length, i - start + 1)

        return max_length
            
            
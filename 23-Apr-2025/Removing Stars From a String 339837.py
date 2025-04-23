# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for char in s:
            if char == '*':
                ans.pop()
            else:
                ans.append(char)
        return ''.join(ans)

        
# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = 0
        for word in words:
            for i in range(len(word)):
                if word[i] not in allowed:
                    break
            else:
                consistent += 1
        return consistent
        
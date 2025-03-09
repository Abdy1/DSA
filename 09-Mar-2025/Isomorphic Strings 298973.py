# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        for i in range(len(s)):
            if s[i] not in s_t:
                if t[i] not in s_t.values():
                    s_t[s[i]] = t[i]
                else:
                    return False
            else:
                if s_t[s[i]] != t[i]:
                    return False
        return True



        
# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_ana = Counter(p)
        k = len(p)
        ans = []
       

        for i in range(len(s)):
            window = s[i:i+k]
            s_ana = Counter(window)
            if p_ana == s_ana:
                ans.append(i)
        return ans



        
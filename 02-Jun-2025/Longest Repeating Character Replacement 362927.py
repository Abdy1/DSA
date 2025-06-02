# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l,mx,cmx = 0,0,0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1
            cmx = max(cmx,count[s[r]])

            if (r-l+1 ) - cmx > k:
                count[s[l]] -= 1
                l += 1
            mx = max(mx,r-l+1)
        return mx



     

        

        
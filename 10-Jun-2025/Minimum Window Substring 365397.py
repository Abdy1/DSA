# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        l,have,need,mn,mnw =0,0,len(Counter(t)),float('inf'),""
        count = Counter(t)
        couns = Counter()
        for r in range(len(s)):
            couns[s[r]] += 1

            if s[r] in count and count[s[r]] == couns[s[r]]:
                have += 1
            
            while have == need:
                if (r-l+1) < mn:
                    mn = r-l+1
                    mnw = s[l:r+1]
                couns[s[l]] -= 1
                if s[l] in count and couns[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        return mnw

    

            


        
       
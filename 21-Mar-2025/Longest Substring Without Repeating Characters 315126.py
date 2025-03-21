# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxx = 0, 0
        seen_chars = set()  
        for r in range(len(s)):
            while s[r] in seen_chars:
                seen_chars.remove(s[l])  
                l += 1 
            
            seen_chars.add(s[r])  
            maxx = max(maxx, r - l + 1)  
        
        return maxx

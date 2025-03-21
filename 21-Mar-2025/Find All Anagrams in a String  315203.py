# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        left = 0
        result = []
        s_count = Counter(s[:len(p)])

        if s_count == p_count:
            result.append(0)
    
 
        for right in range(len(p),len(s)):
            s_count[s[right]] += 1
            s_count[s[right - len(p)]] -= 1

            if s_count[s[right - len(p)]] == 0:
                del s_count[s[right - len(p)]]
            if s_count == p_count:
                result.append(right - len(p) + 1)

        return result


        
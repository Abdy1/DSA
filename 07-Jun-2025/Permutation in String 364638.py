# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0,len(s1)-1
        counter1 = Counter(s1)
        while r < len(s2):
            counter2 = Counter(s2[l:r+1])
            if counter1 == counter2:
                return True
            l += 1
            r += 1

        return False


        
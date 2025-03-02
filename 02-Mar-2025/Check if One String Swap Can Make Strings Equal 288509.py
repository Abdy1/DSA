# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        non_equal = []

        for i in range(len(s2)):
            if s1[i] != s2[i]:
                non_equal.append([s1[i],s2[i]])
                if len(non_equal) > 2:
                    return False
        # print(non_equal)
        if len(non_equal) == 1:
            return False

        return non_equal[0] == non_equal[1][::-1]

        
# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_idx = float('inf')
        for i in range(1,len(strs)):
            for j in range(min(len(strs[i]),len(strs[i-1]))):
                if strs[i][j] != strs[i-1][j]:
                    min_idx = min(min_idx,j)
                    break
        min_len = float('inf')
        if min_idx == float('inf'):
            for str in strs:
                min_len = min(min_len,len(str))
            return strs[0][:min_len]
        else:
            return strs[0][:min_idx]
            


        
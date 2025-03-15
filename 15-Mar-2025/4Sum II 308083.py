# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

from collections import defaultdict

class Solution:
    def fourSumCount(self, A, B, C, D):
        AB_sum = defaultdict(int)
        count = 0
        
        # Store sums of all pairs from A and B in the hash map
        for a in A:
            for b in B:
                AB_sum[a + b] += 1
        
        # For each pair in C and D, check if the negative sum exists in AB_sum
        for c in C:
            for d in D:
                count += AB_sum[-(c + d)]
        
        return count
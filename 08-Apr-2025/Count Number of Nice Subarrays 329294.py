# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cur= 0
        sub= 0
        prefix_sum = defaultdict(int)
        prefix_sum[cur] = 1

        for i in range(len(nums)):
            cur+= nums[i] % 2

            if cur - k in prefix_sum:
                sub+= prefix_sum[cur- k]
            prefix_sum[cur] += 1
        
        return sub


        
        
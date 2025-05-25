# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        pair = 0

        for num in nums:
            if seen[k-num] > 0:
                pair += 1
                seen[k-num] -= 1
            else:
                seen[num] += 1
        return pair
        
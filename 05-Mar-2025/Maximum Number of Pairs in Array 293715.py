# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
    
        pairs = 0
        leftovers = 0
    
        for count in freq.values():
        # Number of pairs is floor division of frequency by 2
            pairs += count // 2
        # Leftovers are the remainder (0 or 1)
            leftovers += count % 2
    
        return [pairs, leftovers]
        
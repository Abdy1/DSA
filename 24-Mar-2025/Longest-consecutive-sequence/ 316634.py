# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sett = set(nums)  # Convert list to set for O(1) lookups
        longest = 0
        
        for num in sett:
            # Only start counting if num is the beginning of a sequence
            if num - 1 not in sett:
                current_num = num
                length = 1
                
                # Count the length of the consecutive sequence starting at num
                while current_num + 1 in sett:
                    current_num += 1
                    length += 1
                
                longest = max(longest, length)  # Update the longest sequence length
        
        return longest

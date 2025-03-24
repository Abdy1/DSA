# Problem: Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sett = set(nums)  
        longest = 0
        
        for num in sett:
            if num - 1 not in sett:
                current_num = num
                length = 1
                
                while current_num + 1 in sett:
                    current_num += 1
                    length += 1
                
                longest = max(longest, length)  
        return longest

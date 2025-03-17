# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_freq = Counter(nums)

        ans = []
        for item, freq in nums_freq.items():
            if freq == 2:
                ans.append(item)
        return ans
        
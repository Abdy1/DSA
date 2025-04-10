# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        item_freq = Counter(nums)
        ONE_THIRD = len(nums)/3

        ans = []

        for item, frequency in item_freq.items():
            if frequency > ONE_THIRD:
                ans.append(item)
        return ans
                
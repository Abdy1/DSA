# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        item_freq = Counter(nums)
        ONE_THIRD = len(nums)/3

        ans = []
        for item, freq in item_freq.items():
            if freq > ONE_THIRD:
                ans.append(item)
        return ans


        
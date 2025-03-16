# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_position = { num : idx for idx, num in enumerate(nums)}

        for value, replacee in operations:
            idx = num_position[value]
            nums[idx] = replacee
            num_position[replacee] = idx
            del num_position[value]
            
        return nums
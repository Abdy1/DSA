# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(1,len(nums)):
            j = i - 1
            key = nums[i]

            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        ans = []
        for i in range(len(nums)):
            if target == nums[i]:
                ans.append(i)

        return ans
        
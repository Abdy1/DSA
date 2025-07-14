# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: sort to bring duplicates together
        res, used = [], [False] * len(nums)
        
        def backtrack(path: List[int]):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Skip duplicates: same as previous and previous not used
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        
        backtrack([])
        return res

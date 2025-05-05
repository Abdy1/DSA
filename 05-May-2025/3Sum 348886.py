# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def sort_(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
        lefty = self.sort_(nums[:mid])
        righty = self.sort_(nums[mid:])

        result = [] 
        l,r = 0,0
        while l < len(lefty) and r < len(righty):
            if lefty[l] > righty[r]:
                result.append(righty[r])
                r += 1
            else:
                result.append(lefty[l])
                l += 1
        result.extend(lefty[l:])
        result.extend(righty[r:])

        return result
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = self.sort_(nums)
        answer = []

        for i, item in enumerate(nums):
            if i > 0 and item == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l < r:
                threeSum = item+nums[l]+nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    answer.append([item,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return answer
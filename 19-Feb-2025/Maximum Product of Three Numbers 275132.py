# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        check = 0
        posCheck = 0
        answer1 = 1
        noSkip = False

        for i in range(len(nums)):
            if nums[i] < 0:
                check += 1     
            else:
                posCheck += 1

        if check >= 2 and posCheck > 0:
            min1 = min(nums)
            nums.remove(min1)
            min2 = min(nums)
            nums.append(min1)
            answer1 =  min1 * min2 * max(nums)     
            noSkip = True       
       

        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)
        nums.remove(max2)
        max3 = max(nums)
        if(noSkip):
                  return max(answer1,(max1*max2*max3))
        return max1*max2*max3
        
        
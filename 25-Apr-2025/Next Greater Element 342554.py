# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for item in nums2:
            while stack and stack[-1] < item:
                next_greater[stack.pop()] = item
            stack.append(item)
        result = []
        for item in nums1:
            result.append(next_greater.get(item,-1))
        return result


   

        
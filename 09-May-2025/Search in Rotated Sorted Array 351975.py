# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
 
        arr1 = [nums[0]]
        arr2 = []

        flag = True
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1] and flag:
                arr1.append(nums[i])
            else:
                flag = False
                arr2.append(nums[i])

        l, r = 0, len(arr1) - 1
        while l <= r:
            mid = (l+r)//2
            res = arr1[mid]
            if res == target:
                return mid
            elif res > target:
                r = mid - 1
            else:
                l = mid + 1

        l, r = 0, len(arr2)-1
        while l <= r:
            mid = (l+r)//2
            res = arr2[mid]
            if res == target:
                return mid + len(arr1)
            elif res > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
        




        
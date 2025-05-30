# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
            """
        n = len(arr)
        zeros = 0
        for item in arr:
                if item == 0:
                    zeros += 1
        
        i =  n - 1
        j = n + zeros -1

        while i >= 0:
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < n: 
                    arr[j] = 0
            i -= 1
            j -= 1
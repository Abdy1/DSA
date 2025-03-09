# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # loop arr1 and collect the ones that are not in arr2 o(n square) time and n  space and time
        remaining = []
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                remaining.append(arr1[i])
        



        # sort costs nsquare
        if remaining:
            max_number = max(remaining)
            distribution = [0] * (max_number + 1)

        
            for i in range(len(remaining)):
                distribution[remaining[i]] += 1

            sorted_remaining = []

            for i in range(len(distribution)):
                sorted_remaining.extend([i]*distribution[i])

    
        #   go through arr2 and for each element look in arr1 and append
        ans = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    ans.append(arr1[j])
        if remaining:
            ans.extend(sorted_remaining)
        return ans


        
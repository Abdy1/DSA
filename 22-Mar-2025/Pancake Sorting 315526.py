# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        
        # Iterate over the entire array
        for i in range(n, 1, -1):
            # Find the index of the maximum element in the unsorted portion
            max_index = arr.index(max(arr[:i]))
            
            if max_index == i - 1:
                continue  # It's already in the correct place
            
            # Step 1: Bring the maximum element to the front
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
                res.append(max_index + 1)
            
            # Step 2: Move the maximum element to its correct position
            arr[:i] = arr[:i][::-1]
            res.append(i)
        
        return res

            
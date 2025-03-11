# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while numbers[l] + numbers[r] != target:
            summ = numbers[l] + numbers[r]

            if summ > target:
                r -= 1
            else:
                l += 1
        return [l+1,r+1]
        
# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        found = False
        for i in range(left,right+1):
            found = any(range[0] <= i <= range[1] for range in ranges)
            if not found:
                return found
        return found

        
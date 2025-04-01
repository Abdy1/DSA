# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count = 0
        visit = set()
        max_number = 0

        for n in nums:
            if n not in visit:
                count += 1
                visit.add(n)

            if count == 3:
                return n
            
            max_number = max(max_number, n)
            
        return max_number
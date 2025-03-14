# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        summ = sum(item for item in nums if item%2 == 0)
        for query in queries:
            if nums[query[1]] %2 == 0:
                summ -= nums[query[1]]
            improvement = nums[query[1]] + query[0]
            nums[query[1]] = improvement
            if improvement%2 == 0:
                summ += improvement
            ans.append(summ)
        return ans

        
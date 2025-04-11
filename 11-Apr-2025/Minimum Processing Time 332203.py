# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        sectors = self.splitt(tasks, len(tasks)//len(processorTime))
        ans = -1
        left = 0
        right = len(sectors) - 1
        while right >= 0:
            ans = max(ans,sectors[left][-1] + processorTime[right])
            left += 1
            right -= 1
        return ans


    def splitt(self, lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]


        
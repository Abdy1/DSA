# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        start_with_index = [(interval[0], i) for i, interval in enumerate(intervals)]
        start_with_index.sort() 
        starts = [start for start, _ in start_with_index]

        result = []
        for interval in intervals:
            end = interval[1]
            idx = bisect_left(starts, end)
            if idx < n:
                result.append(start_with_index[idx][1])
            else:
                result.append(-1)

        return result
            
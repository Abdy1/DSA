# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize an empty result list
        merged = []

        # Step 3: Iterate through the sorted intervals
        for interval in intervals:
            # If the merged list is empty or the current interval does not overlap with the last merged interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge the current interval with the last one in the merged list
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
        
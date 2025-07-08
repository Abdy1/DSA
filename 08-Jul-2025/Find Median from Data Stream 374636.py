# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max heap (invert values to simulate)
        self.large = []  # Min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # Balance: move the largest of small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Maintain size property
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2

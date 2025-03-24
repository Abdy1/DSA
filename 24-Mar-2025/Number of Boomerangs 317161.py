# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for p1 in points:
            distance_count = defaultdict(int)
            for p2 in points:
                if p1 != p2:
                    dist = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
                    distance_count[dist] += 1
            for count in distance_count.values():
                res += count * (count - 1)
        return res
        
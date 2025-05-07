# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc_hour(val):
            total = 0
            for item in piles:
                total += math.ceil(item/val)
            return total

        l, r = 1, max(piles) 
        while l <= r:  
            mid = (l+r)//2
            if calc_hour(mid) > h:
                l = mid + 1
            else:
                r = mid - 1
        return l


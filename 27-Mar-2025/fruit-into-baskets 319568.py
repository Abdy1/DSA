# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        maxx = 0
        left = 0
        basket = {}

        for right in range(len(fruits)):
            basket[fruits[right]] = right
            while len(basket) > 2:
                left = min(basket.values()) + 1
                del basket[fruits[left - 1]]
            maxx = max((right - left + 1), maxx)
        return maxx



            


        
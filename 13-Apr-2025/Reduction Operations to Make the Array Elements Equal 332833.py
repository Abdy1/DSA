# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def sortt(self, lst):
        maxx = max(lst)
        count = [0] * (maxx + 1)

        for itm in lst:
            count[itm] += 1
        res = []
        for val, freq in enumerate(count):
            res.extend([val] * freq)
        return res

    def reductionOperations(self, nums: List[int]) -> int:
        nums = self.sortt(nums)
        unique = list(set(nums))
        unique.sort()
        freq_dict = Counter(nums)
        steps = 0
        for i in range(len(unique)):
            num = unique[i]
            steps += freq_dict[num] * i  
        
        return steps  

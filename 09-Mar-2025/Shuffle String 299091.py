# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
      
        items = list(zip(indices,s))
        items = sorted(items, key=lambda x:x[0])
        ans = []
        for item in items:
            ans.append(item[1])
        ans = "".join(ans)
        return ans
        
# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [("",0,0)]
        result = []

        while stack:
            seq, ope, clo = stack.pop()
            if len(seq) == 2*n:
                result.append(seq)
            else:
                if ope < n:
                    stack.append((seq+'(',ope + 1, clo))
                if clo < ope:
                    stack.append((seq+')',ope,clo+1))
        return result
       
            
# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                item = stack.pop()
                answer[item] =i-item
            stack.append(i)
        return answer

        

        
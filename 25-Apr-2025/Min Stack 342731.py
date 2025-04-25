# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minn:
            val = min(val, self.minn[-1])
        self.minn.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minn.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minn[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
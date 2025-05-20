# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

from collections import deque
def work(messages):
    seen = set()
    listt = deque()
    
    for name in reversed(messages):
        if name not in seen: 
            seen.add(name)
            listt.appendleft(name)
    return listt
t = int(input())
messages = [input().strip() for _ in range(t)]
result = work(messages)
print('\n'.join(reversed(result)))
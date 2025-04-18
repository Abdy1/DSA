# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

i = 0
j = 0
ans = []

while i < n and j < m:
    while  i < n and a[i] < b[j]:
        i += 1
    ans.append(i)
    j += 1
while j < m:
    j += 1
    ans.append(i)
print(*ans)
    

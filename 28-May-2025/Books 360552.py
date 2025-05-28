# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
a = list(map(int,input().split()))

slow = 0
run = 0
max_book = 0
for fast in range(len(a)):
    run += a[fast]
    while run > t:
        run -= a[slow]
        slow += 1
    max_book = max(max_book, fast - slow + 1)

print(max_book)
        
 
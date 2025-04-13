# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if k == 0:
    if a[0] > 1:
        print(a[0] - 1)
    else:
        print(-1)
else:
    if k == n or a[k] > a[k - 1]:
        print(a[k - 1])
    else:
        print(-1)

# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n, m = map(int,input().split())

forward = False

for i in range(n):
    if i % 2 == 0:
        print("".join(['#']  * m))
    else:
        times = m - 1
        if forward:
            print("#"+"".join(['.'] * times))
        elif not forward:
            print("".join(['.'] * times)+"#")
        forward = not forward


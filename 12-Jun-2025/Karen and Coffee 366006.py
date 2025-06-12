# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B


def sol():
    n , k , m = map(int , input().split())
    sums , sum = [0]*200005 , [0] * 200005
    while n > 0:
        n -= 1
        l , r = map(int , input().split())
        sums[l] += 1
        sums[r+1] -= 1
    for i in range(1,200005):
        sums[i] += sums[i-1]
        if sums[i] >= k:
            sum [i] = 1
  

    for i in range(1,200005):
        sum[i] += sum[i-1]

    while m > 0:
        m -= 1
        l , r = map(int , input().split())
        print(sum[r] - sum[l-1])           

if __name__ == "__main__":  
    T = 1
    for _ in range(T):  
        sol()
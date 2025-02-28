# Problem: Watermelon - https://codeforces.com/problemset/problem/4/A

w = int(input())  # Input the weight of the watermelon

# Check if the weight is even and at least 4
if w % 2 == 0 and w >= 4:
    print("YES")
else:
    print("NO")

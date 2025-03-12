# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

matrix = []
coordinate = []
for i in range(5):
    columns = list(map(int,input().split()))
    matrix.append(columns)
    if 1 in columns:
        coordinate.append(i)
        coordinate.append(columns.index(1))

print(abs(2-coordinate[0]) + abs(2-coordinate[1]))


# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

password = input()
found = False
n = int(input())
barks = []
for _ in range(n):
    barks.append(input())


for i in range(len(barks)):
    for j in range(i,len(barks)):
        if password in barks[i]+barks[j] or password in barks[j]+barks[i]:
            print("YES")
            found = True
            break
    if found:
        break
if not found:
    print("NO")

    
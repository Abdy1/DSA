# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true



if __name__ == '__main__':
    ans = []
    N = int(input())
    
    for _ in range(N):
        command = list(input().split())
        if "insert" in command:
            ans.insert(int(command[1]),int(command[2]))
        elif "print" in command:
            print(ans)
        elif "remove" in command:
            ans.remove(int(command[1]))
        elif "append" in command:
            ans.append(int(command[1]))
        elif "sort" in command:
            ans.sort()
        elif "pop" in command:
            ans.pop()
        elif "reverse" in command:
            ans.reverse()            
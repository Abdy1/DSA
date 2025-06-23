# Problem: C - Get in the Center, You Weirdos! - https://codeforces.com/gym/617023/problem/C

def min_moves_to_center(test_cases):
    results = []
    for n in test_cases:
        k = n // 2
        total_moves = (4 * k * (k + 1) * (2 * k + 1)) // 3
        results.append(total_moves)
    return results


t = int(input())
test_cases = [int(input()) for _ in range(t)]
answers = min_moves_to_center(test_cases)
for ans in answers:
    print(ans)

def solve(n):
    res = n
    if n * 10 + 4 <= N:
        res = max(res, solve(n * 10 + 4))
    if n * 10 + 7 <= N:
        res = max(res, solve(n * 10 + 7))
    return res

N = int(input())
print(solve(0))
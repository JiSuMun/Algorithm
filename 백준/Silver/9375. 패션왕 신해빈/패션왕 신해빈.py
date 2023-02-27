import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    n = int(input())
    c = {}
    clothes = [input().rstrip().split() for _ in range(n)]
    for k, v in clothes:
        c[v] = c.get(v, 0) + 1
    res = 1
    for i in c:
        res *= (c[i] + 1)
    print(res-1)
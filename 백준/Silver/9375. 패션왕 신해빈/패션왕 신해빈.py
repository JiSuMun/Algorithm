# 44ms
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    n = int(input())
    li = []
    for _ in range(n): li.append(input().rstrip().split())
    a = set()
    c = []
    for i in range(n):
        a.add(li[i][1])
        c.append(li[i][1])
    res = 1
    for j in a:
        res *= c.count(j) + 1
    print(res-1)
# 44ms
# import sys
# input = sys.stdin.readline
# T = int(input())
# for t in range(T):
#     n = int(input())
#     c = {}
#     clothes = [input().rstrip().split() for _ in range(n)]
#     for k, v in clothes:
#         c[v] = c.get(v, 0) + 1
#     res = 1
#     for i in c:
#         res *= (c[i] + 1)
#     print(res-1)
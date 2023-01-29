import sys
input = sys.stdin.readline
N, K = map(int, input().split())
idx = 0
li = [i for i in range(1, N+1)]
res = []
while li:
    idx += K - 1
    if idx >= len(li):
        idx %= len(li)
    res.append(str(li.pop(idx)))
print("<", ", ".join(res), ">", sep="")
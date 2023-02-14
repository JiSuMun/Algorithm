import sys
input = sys.stdin.readline
N = int(input())
li = []
d = {}
best = []
for _ in range(N):
    li.append(input().rstrip())
for i in list(set(li)): d[i] = li.count(i)
for k in d.keys():
    if d[k] == max(d.values()):
        best.append(k)
best.sort()
print(best[0])
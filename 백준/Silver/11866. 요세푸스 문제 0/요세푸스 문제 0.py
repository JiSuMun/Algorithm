import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
li = deque()
res = []
for i in range(1, N+1):
    li.append(i)
while li:
    for j in range(K-1):
        li.append(li.popleft())
    res.append(li.popleft())
print('<', end='')
print(', '.join(map(str, res)), end='')
print('>')
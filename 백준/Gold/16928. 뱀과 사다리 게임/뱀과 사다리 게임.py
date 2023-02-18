import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
di = {}
for _ in range(N+M):
    a, b = map(int, input().split())
    di[a] = b

d = deque([1])
board = [100]*101
visited = [False]*101
board[1] = 0
visited[1] = True

while d:
    g = d.popleft()
    for i in range(1, 7):
        next = g + i
        if next > 100: continue
        if next in di:
            next = di[next]
        if visited[next]: continue # False이다
        d.append(next)
        visited[next] = True 
        board[next] = board[g] + 1
print(board[100])
import sys
N, M = map(int, input().split())
di = {}
for _ in range(N+M):
    a, b = map(int, input().split())
    di[a] = b
q = []
q.append(1)
visited = [False]*101
board = [100]*101
board[1] = 0
visited[1] = True
while q:
  v = q.pop(0)
  for i in range(1, 7):
    next = v + i
    if next > 100: continue
    if next in di:
      next = di[next]
    if visited[next]: continue
    q.append(next)
    visited[next] = True
    board[next] = board[v] + 1
print(board[100])
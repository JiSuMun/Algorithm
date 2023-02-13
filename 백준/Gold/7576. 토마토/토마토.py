import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
box = []
cnt = -1
M, N = map(int, input().split())
for i in range(N):
    box.append(list(map(int, input().split())))
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))
while queue:
    cnt+=1
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if box[nx][ny] == 0:
                    box[nx][ny] = 1
                    queue.append((nx, ny))
for i in box:
    if 0 in i:
        cnt =- 1
        break
print(cnt)
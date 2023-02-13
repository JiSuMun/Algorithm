import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
d = deque()
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
def BFS():
    while d:
        z, x, y = d.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if tomato[nz][nx][ny] == 0:
                    tomato[nz][nx][ny] = tomato[z][x][y] + 1 # 익지 않은 토마토 익힘 처리
                    d.append((nz, nx, ny))
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                d.append((i, j, k)) # 익은 토마토 주변에 있는 익지 않은 토마토를 익힘 처리해야함
BFS()
day = 0
for i in tomato:
    for j in i:
        for k in j:
            if k==0:
                print(-1) # 모두 익지 못하는 상황
                exit(0) # 코드 종료
        day = max(day,max(j)) # 모두 익은 상태
print(day-1)
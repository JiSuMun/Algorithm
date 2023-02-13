import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
q = deque([])
for y in range(N):
    for x in range(M):
        if(tomato[y][x] == 1):
            q.append([y,x])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def in_range(y,x):
    return 0 <= y < N and 0 <= x < M
cnt = 0
while q:
    new_q = deque([])
    while(q):
        y, x = q.pop()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if in_range(ny,nx) and tomato[ny][nx] == 0:
                new_q.append([ny,nx])
                tomato[ny][nx] = 1
    cnt += 1
    q = new_q

for y in range(N):
    for x in range(M):
        if(tomato[y][x] == 0):
            print(-1)
            exit(0)
print(cnt-1)
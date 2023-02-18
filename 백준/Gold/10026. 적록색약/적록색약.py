import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
field = [list(input().rstrip()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
a, b = 0, 0 # 적록색맹 아닌경우, 적록색맹인 경우
def DFS(x, y):
    visited[x][y] = True
    cur = field[x][y]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == False:
                if field[nx][ny] == cur:
                    DFS(nx, ny)
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            DFS(i,j)
            a += 1
for i in range(N):
    for j in range(N):
        if field[i][j] == 'R':
            field[i][j] = 'G'
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            DFS(i, j)
            b += 1
print(a, b)
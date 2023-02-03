import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def DFS(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 1:
                board[nx][ny] = -1
                DFS(nx, ny)
    return

for _ in range(T):
    M, N, K = map(int,input().split())
    board = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                DFS(i, j)
                cnt += 1
    print(cnt)
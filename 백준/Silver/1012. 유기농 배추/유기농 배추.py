# 76ms
import sys 
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
def BFS(board, a, b):
    queue = deque()
    queue.append((a,b))
    board[a][b] = 0 # 방문처리
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    queue.append((nx, ny))
    return

for _ in range(T):
    cnt = 0
    M, N, K = map(int,input().split())
    board = [[0]*N for _ in range(M)]
    for i in range(K):
        x, y = map(int, input().split())
        board[x][y] = 1
    
    for a in range(M):
        for b in range(N):
            if board[a][b] == 1:
                BFS(board, a, b)
                cnt += 1
    print(cnt)
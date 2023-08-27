from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 아기상어의 좌표, 사이즈 초기값 (아기 상어의 초기 사이즈는 2)
s_x, s_y, s_size = 0, 0, 2

# 상어의 위치 좌표를 미리 찾아주고 값을 0으로 바꿔줌
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            s_x, s_y = i, j
            board[i][j] = 0

def bfs(x, y, size):
    distance = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다. => 정렬 필요
    li = []
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 사이즈가 같고, 방문하지 않았으면 이동 가능한 좌표
                if board[nx][ny] <= size and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1

                    # 물고기가 있으며 먹을 수 있는 크기 (같은 크기는 포함 X)
                    if board[nx][ny] != 0 and board[nx][ny] < size:
                        li.append((nx, ny, distance[nx][ny]))
    # distance, x, y 순 오름차순
    return sorted(li, key=lambda x: (x[2], x[0], x[1]))

cnt = 0
res = 0
while True:
    shark = bfs(s_x, s_y, s_size)
    # 먹을 수 있는 물고기가 없다면 종료
    if len(shark) == 0: break
    s_x, s_y, dis = shark[0]
    cnt += 1
    # 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
    if cnt == s_size: s_size += 1; cnt = 0

    board[s_x][s_y] = 0
    res += dis

print(res)
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
def BFS(i, j):
    q = [[i, j]]
    graph[i][j] = 0
    while q:
        y, x = q.pop(0)
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
                q.append([ny, nx])
                graph[ny][nx] = 0

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                BFS(i, j)
                cnt += 1
    print(cnt)
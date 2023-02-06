import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
# dx = [1, -1, 0, 0, 1, -1, 1, -1]
# dy = [0, 0, -1, 1, -1, 1, 1, -1]
def BFS(x, y):
    graph[x][y] = 0
    d = deque()
    d.append([x, y])
    while d:
        a, b = d.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                d.append([nx, ny])
while 1:
    w, h = map(int, input().split())
    if w == h == 0: break
    graph = []
    res = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1:
                BFS(x, y)
                res += 1
    print(res)
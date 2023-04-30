from collections import deque
def solution(maps):
    n = len(maps)
    res = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    def bfs(x, y):
        d = deque()
        d.append((x, y))
        
        while d:
            x, y = d.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= len(maps[0]): continue 
                if maps[nx][ny] == 0: continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    d.append((nx, ny))
        return maps[n-1][len(maps[0])-1]
    res = bfs(0, 0)
    return -1 if res == 1 else res
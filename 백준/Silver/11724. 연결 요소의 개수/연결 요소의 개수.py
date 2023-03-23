import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000)

def dfs(start, depth):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문처리 위한 리스트
visited = [False] * (N + 1)
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = True # 방문처리
        else: # 연결 된 점이 있다면
            dfs(i, 0)
            cnt += 1
print(cnt)
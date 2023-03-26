import sys
input = sys.stdin.readline
from collections import deque
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(V):
    visited[V] = 1
    dfs_li.append(V)
    for i in sorted(graph[V]):
        if not visited[i]:
            dfs(i)

def bfs(V):
    visited[V] = 1
    d = deque([V])
    while d:
        a = d.popleft()
        bfs_li.append(a)
        for j in sorted(graph[a]):
            if not visited[j]:
                visited[j] = 1
                d.append(j)

dfs_li = []
bfs_li = []
visited = [0] * (N+1)
dfs(V)
visited = [0] * (N+1)
bfs(V)
print(*dfs_li)
print(*bfs_li)
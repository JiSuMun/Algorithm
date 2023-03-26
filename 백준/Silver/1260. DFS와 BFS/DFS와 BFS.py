import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def dfs(graph, V):   
    visited[V] = 1
    print(V, end=' ')
    for i in graph[V]:
        if not visited[i]:
            dfs(graph, i)

def bfs(graph, V):   
    d = deque([V])
    visited[V] = 1
    while d:
        a = d.popleft()
        print(a, end=' ')
        for i in graph[a]:
            if not visited[i]:
                d.append(i)
                visited[i] = 1
visited = [0] * (N+1)
dfs(graph, V)
print('')
visited = [0] * (N+1)
bfs(graph, V)
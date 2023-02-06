import sys
input = sys.stdin.readline
N = int(input())
C = int(input())
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(C):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def DFS(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            DFS(i)
DFS(1)
print(sum(visited)-1)
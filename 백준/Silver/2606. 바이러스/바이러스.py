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
    res = 0
    stack = [start]
    visited[start] = 1
    while stack:
        c = stack.pop()
        for i in graph[c]:
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
                res += 1
    print(res)
DFS(1)
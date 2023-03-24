# wires는 길이가 n-1인 정수형 2차원 배열
from collections import deque, defaultdict

def bfs(graph, start, visited):
    cnt = 1 # 시작한 노드는 연결된 노드가 1개로 시작됨
    d = deque([start])
    visited[start] = 1    
    while d:
        b = d.popleft()
        for i in graph[b]:
            if not visited[i]:
                d.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

def solution(n, wires):
    wire = deque(wires)
    res = n # n 변경하지 않기 위해
    for _ in range(len(wires)):
        a = wire.popleft()
        visited = [0] * (n+1)
        graph = defaultdict(list)
        cnt_li = []
        for v1, v2 in wire:
            graph[v1].append(v2)
            graph[v2].append(v1)
        for i in range(1, n+1):
            if not visited[i]:
                cnt_li.append(bfs(graph, i, visited))
        res = min(abs(cnt_li[0] - cnt_li[1]), res)
        wire.append(a)
    return res


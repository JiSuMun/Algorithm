from heapq import heappop, heappush

def solution(n, costs):
    graph = [[] for _ in range(n)]
    for island1, island2, cost in costs:
        graph[island1].append((island2, cost))
        graph[island2].append((island1, cost))
    visited = [False] * n
    # 첫 번째 섬, 비용
    heap = [(0, 0)]
    res = 0

    while heap:
        cost, island = heappop(heap)
        if visited[island]: continue
        visited[island] = True
        res += cost
        for n_island, n_cost in graph[island]:
            if not visited[n_island]:
                heappush(heap, (n_cost, n_island))

    return res
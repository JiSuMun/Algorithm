import heapq

def solution(n, costs):
    graph = [[] for _ in range(n)]
    for island1, island2, cost in costs:
        graph[island1].append((island2, cost))
        graph[island2].append((island1, cost))

    visited = [False] * n
    heap = [(0, 0)]
    res = 0

    while heap:
        cost, island = heapq.heappop(heap)
        if visited[island]: continue
        visited[island] = True
        res += cost
        for n_island, n_cost in graph[island]:
            if not visited[n_island]:
                heapq.heappush(heap, (n_cost, n_island))

    return res

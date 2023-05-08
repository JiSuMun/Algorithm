from collections import defaultdict
def solution(tickets):
    res = []
    graph = defaultdict(list)
    for (start, end) in tickets:
        graph[start].append(end)
    for ap in graph.keys():
        graph[ap].sort(reverse=True)
    stack = ["ICN"]
    while stack:
        air = stack.pop()
        if air not in graph or not graph[air]:
            res.append(air)
        else:
            stack.append(air)
            stack.append(graph[air].pop())
    return res[::-1]
from collections import deque
def solution(begin, target, words):
    if target not in words: return 0
    n = len(begin)
    graph = {}
    words.append(begin)
    for word in words:
        graph[word] = []
        for w in words:
            if word == w: continue
            cnt = 0
            for i in range(n):
                if word[i] != w[i]: cnt += 1
                if cnt > 1: break
            if cnt == 1: graph[word].append(w)
    d = deque([(begin, 0)])
    visited = set()
    while d:
        cur, change = d.popleft()
        if cur == target: return change
        for next in graph[cur]:
            if next not in visited:
                visited.add(next)
                d.append((next, change+1))
    return 0
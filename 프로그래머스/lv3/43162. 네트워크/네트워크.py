def dfs(v, visited, computers):
    visited[v] = True
    for nei in range(len(computers)): 
        if not visited[nei] and computers[v][nei]: 
            dfs(nei, visited, computers)

def solution(n, computers):
    cnt = 0   
    visited = [False] * n   

    for node_idx in range(n):
        if not visited[node_idx] :
            dfs(node_idx, visited, computers)
            cnt += 1 

    return cnt
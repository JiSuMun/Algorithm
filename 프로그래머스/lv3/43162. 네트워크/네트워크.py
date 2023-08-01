def dfs(idx, visited, computers):
    visited[idx] = True
    for nei in range(len(computers)): 
        if not visited[nei] and computers[idx][nei]: 
            dfs(nei, visited, computers)

def solution(n, computers):
    cnt = 0   
    visited = [False] * n   

    for idx in range(n):
        if not visited[idx] :
            dfs(idx, visited, computers)
            cnt += 1 

    return cnt
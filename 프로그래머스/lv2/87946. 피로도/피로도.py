# k => 현재 피로도
# dungeons[i][0] => 최소 필요 피로도
# dungeons[i][1] => 소모 피로도
# NameError: not defined => global 사용
# 미리 visited를 len(dungeons) 사용해줬으나 NameError로 새로운 변수 사용해줌
res = 0
visited = []
def solution(k, dungeons):
    global res, visited
    visited = [0] * len(dungeons)
    dfs(k, 0, dungeons)
    return res
def dfs(k, cnt, dungeons):
    global res   
    if cnt > res:
        res = cnt
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            dfs(k-dungeons[i][1], cnt+1, dungeons)
            visited[i] = 0 # 복구
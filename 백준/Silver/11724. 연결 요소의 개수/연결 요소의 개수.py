# 11724
# pypy: 
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seqnum = [0] * (N+1) # visited
seq = 1
ans = N # 반복하면서 노드의 개수를 줄여야 할 때 사용하는 변수, N 값이 변하지 않게 따로 변수 선언

for _ in range(M):
    if ans == 1:
        input()
        continue
    valid = True
    u, v = map(int, input().split())
    # 연결점 1 표시 (True 표시와 같은 의미)
    if seqnum[u] == 0 and seqnum[v] == 0:
        seqnum[u] = seqnum[v] = seq
        seq += 1
    elif seqnum[u] == 0:
        seqnum[u] = seqnum[v]
    elif seqnum[v] == 0:
        seqnum[v] = seqnum[u]
    else:
        if seqnum[u] == seqnum[v]:
            valid = False
        else:
            low_s = min(seqnum[u], seqnum[v])
            high_s = max(seqnum[u], seqnum[v])
            for i in range(1, N+1):
                if seqnum[i] == high_s:
                    seqnum[i] = low_s
    if valid:
        ans -= 1

print(ans)
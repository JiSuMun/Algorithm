import sys
from collections import deque
input=sys.stdin.readline
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    P = deque(map(int, input().split())) # 중요도
    queue = deque([0 for i in range(N)])# 위치 저장 리스트
    queue[M] = 1
    cnt = 0
    while 1:
        if P[0] == max(P): # 가장 큰 값이면 cnt에 1을 더해주고 삭제
            cnt += 1
            if queue[0] == 1: # 가장 큰 값이면서 내가 찾을 값이면 cnt출력하고 break
                print(cnt)
                break
            else:
                P.popleft()
                queue.popleft()
        else: # 가장 큰 값이 아니라면 맨 뒤에 넣어주고 삭제
            P.append(P.popleft())
            queue.append(queue.popleft())
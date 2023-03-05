# from heapq import heappush, heappop
# def solution(scoville, K):
#     heap = []
#     for i in scoville: heappush(heap, i)
#     cnt = 0
#     while heap[0] < K:
#         try: heappush(heap, heappop(heap) + heappop(heap) * 2)
#         except: return -1
#         cnt += 1
#     return cnt
from collections import deque

def solution(S, K):
    res = 0
    mix_s = deque()
    S.sort()
    scoville = deque(i for i in S)
    while (scoville and scoville[0] < K) or (mix_s and mix_s[0] < K):
        res += 1
        if len(scoville) + len(mix_s) <= 1: return -1
        food = [0]*2
        for i in range(2):
            if scoville and mix_s:
                if scoville[0] < mix_s[0]: food[i] = scoville.popleft()
                else: food[i] = mix_s.popleft()
            elif scoville: food[i] = scoville.popleft()
            else: food[i] = mix_s.popleft()
        mix_s.append(food[0]+food[1]*2)
    return res
                    
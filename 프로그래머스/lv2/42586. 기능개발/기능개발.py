# def solution(progresses, speeds):
#     res = []
#     while progresses:
#         cnt = 0
#         while progresses and progresses[0] >= 100:
#             cnt += 1
#             progresses.pop(0)
#             speeds.pop(0)
#         progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
#         if cnt: res.append(cnt)        
#     return res
import math
from collections import deque
def solution(progresses, speeds):
    res = []
    p = deque([math.ceil((100-a)/b) for a, b in zip(progresses, speeds)])
    cnt = 1
    a = p.popleft()
    while p:
        if p[0] <= a:
            p.popleft()
            cnt += 1
        else:
            a = p.popleft()
            res.append(cnt)
            cnt = 1
    res.append(cnt)        
    return res
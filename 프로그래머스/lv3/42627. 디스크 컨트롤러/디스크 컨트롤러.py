from heapq import heappush, heappop
def solution(jobs):
    res, now, cnt = 0, 0, 0 # 평균값, 현재시간, 작업개수
    start = -1 # 앞에 완료한 작업의 시작 시간
    heap = []
    while cnt < len(jobs):
        for j in jobs:
            if start < j[0] <= now: heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            cur = heappop(heap)
            start = now
            now += cur[0]
            res += (now - cur[1])
            cnt += 1
        else: now += 1
    return int(res/len(jobs))
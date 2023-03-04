from heapq import heappush, heappop
def solution(scoville, K):
    heap = []
    for i in scoville: heappush(heap, i)
    cnt = 0
    while heap[0] < K:
        try: heappush(heap, heappop(heap) + heappop(heap) * 2)
        except: return -1
        cnt += 1
    return cnt
from heapq import heappush, heappop, nlargest, heapify
def solution(operations):
    answer = []
    heap = []
    for i in operations:
        if i[0] == 'I': heappush(heap, int(i[2:]))
        else:
            if len(heap) == 0: pass
            elif i[2] == '-': heappop(heap)
            else:
                heap = nlargest(len(heap), heap)[1:]
                heapify(heap)
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
    return answer
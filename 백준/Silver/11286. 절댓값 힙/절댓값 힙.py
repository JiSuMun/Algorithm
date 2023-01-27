import sys
import heapq
input = sys.stdin.readline
N = int(input())
p_heap = [] # 양수
m_heap = [] # 음수
for _ in range(N):
    x = int(input())
    if x:
        if x > 0:
            heapq.heappush(p_heap, x) # 양수에 추가
        else:
            heapq.heappush(m_heap, -x) # 음수에 추가
    else:
        if p_heap:
            if m_heap:
                if p_heap[0] < abs(-m_heap[0]):
                # if p_heap[0] < m_heap[0]:
                    print(heapq.heappop(p_heap))
                else:
                    print(-heapq.heappop(m_heap))
            else:
                print(heapq.heappop(p_heap))
        else:
            if m_heap:
                print(-heapq.heappop(m_heap))
            else:
                print(0)
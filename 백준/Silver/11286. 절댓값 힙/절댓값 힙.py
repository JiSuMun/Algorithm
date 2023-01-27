import sys
import heapq
input = sys.stdin.readline
N = int(input())
abs_h = []
for _ in range(N):
    x= int(input())
    if x != 0:
        heapq.heappush(abs_h, (abs(x), x))
    else:
        try:
            print(heapq.heappop(abs_h)[1])
        except:
            print(0)
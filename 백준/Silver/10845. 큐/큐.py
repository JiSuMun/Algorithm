import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque()
for _ in range(N):
    order = input().split()
    o = order[0]
    if o == 'push': queue.append(order[1])
    elif o == 'pop': print(queue.popleft()) if queue else print(-1)        
    elif o == 'size': print(len(queue))
    elif o == 'empty': print(1) if len(queue) == 0 else print(0)       
    elif o == 'front': print(queue[0]) if queue else print(-1)
    elif o == 'back': print(queue[-1]) if queue else print(-1)
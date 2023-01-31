import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
d = deque()
for _ in range(N):
    order = input().split()
    o = order[0]
    if o == 'push_front': d.appendleft(order[1])
    elif o == 'push_back': d.append(order[1])
    elif o == 'pop_front': print(d.popleft()) if d else print(-1)
    elif o == 'pop_back': print(d.pop()) if d else print(-1)      
    elif o == 'size': print(len(d))
    elif o == 'empty': print(1) if len(d) == 0 else print(0)       
    elif o == 'front': print(d[0]) if d else print(-1)
    elif o == 'back': print(d[-1]) if d else print(-1)
import sys
input = sys.stdin.readline
N = int(input())
d = []
for _ in range(N):
    order = input().rstrip().split()
    o = order[0]
    if o == 'push_front': d.insert(0, order[1])
    elif o == 'push_back': d.append(order[1])
    elif o == 'pop_front': print(d.pop(0) if d else -1)
    elif o == 'pop_back': print(d.pop() if d else -1)    
    elif o == 'size': print(len(d))
    elif o == 'empty': print(0 if d else 1)       
    elif o == 'front': print(d[0] if d else -1)
    elif o == 'back': print(d[-1] if d else -1)
import sys
input = sys.stdin.readline
from collections import deque
T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    flag = 1
    arr = input().rstrip()
    d = deque(arr[1:-1].split(','))
    if n == 0: d = deque()
    R = 0
    for i in range(len(p)):
        if p[i] == 'R': R += 1
        elif p[i] == 'D':
            if len(d) == 0: print('error'); flag = 0; break
            else:
                if R % 2 == 0: d.popleft() # 뒤집기를 짝수로 시행하면 원상태
                else: d.pop()
    if flag == 0: continue
    else:
        if R % 2 == 0: print('[' + ','.join(d) + ']')
        else: d.reverse(); print('[' + ','.join(d) + ']')
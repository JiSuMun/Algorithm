import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
li = []
for n in range(M, N+1):
    if n == 1:
        continue
    for i in range(2, n):
        if n % i  == 0:
            break
    else:
        li.append(n)
if len(li) >= 1:
    print(f'{sum(li)}\n{min(li)}')
else:
    print(-1)
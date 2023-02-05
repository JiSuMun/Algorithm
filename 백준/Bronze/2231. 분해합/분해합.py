import sys
input=sys.stdin.readline
N = int(input())
res = 0
for i in range(max(1, N-len(str(N))*9), N+1):
    if sum(map(int, str(i))) + i == N: res = i; break
print(res)
import sys
input = sys.stdin.readline
N = int(input())
res = 1
cnt = 0
idx = -1
for i in range(1, N+1): res *= i
while 1:
    if str(res)[idx] == '0': cnt += 1; idx -= 1
    else: break
print(cnt)
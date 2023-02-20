import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N-1, -1, -1):
    cnt += K // A[i]
    K %= A[i]
print(cnt)
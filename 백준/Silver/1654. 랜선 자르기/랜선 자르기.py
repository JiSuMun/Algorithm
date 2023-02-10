import sys
input = sys.stdin.readline
K, N = map(int, input().split())
l = [int(input()) for _ in range(K)]
start, end = 1, sum(l) // N
while start <= end:
    mid = (start + end) // 2
    if sum([i//mid for i in l]) >= N: start = mid + 1
    else: end = mid -1
print(end)
from itertools import accumulate
import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))
arr = [None] * (N +1)
arr[0] = [0 for i in range(M+1)]
for i in range(1, N+1):
    arr[i] = accumulate(list(map(int, input().split())), initial=0)
    arr[i] = [x+y for x, y in zip(arr[i-1], arr[i])]
K = int(input().rstrip())
ans = [None] * K
for n in range(K):
    i, j, x, y = list(map(int, input().split()))
    ans[n] = arr[x][y] - arr[x][j-1] - arr[i-1][y] + arr[i-1][j-1]
print(*ans, sep = '\n')

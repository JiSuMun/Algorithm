import sys

input = sys.stdin.readline


N, K = map(int, input().split())
arr = list(map(int, input().split()))

p_sum = sum(arr[:K])
res = [p_sum]

for i in range(N - K):
    p_sum = p_sum - arr[i] + arr[i + K]
    res.append(p_sum)

print(max(res))

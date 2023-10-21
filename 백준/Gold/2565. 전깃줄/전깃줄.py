import sys

input = sys.stdin.readline

n = int(input())
cable = sorted([list(map(int, input().split())) for _ in range(n)])

# 증가하지 않더라도 해당 순서만 포함된 수열이 있기 때문에 전체 초기값 1
dp = [1] * n
for i in range(n):
    for j in range(i):
        if cable[i][1] > cable[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
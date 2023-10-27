import sys

input = sys.stdin.readline

N = int(input())
house = [[0 for _ in range(N)]]
for _ in range(N):
    house.append(list(map(int, input().split())))

# 가로, 세로, 대각선
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N + 1)]

# 시작 위치
dp[1][1] = [1, 0, 0]

for i in range(1, N + 1):
    for j in range(1, N):
        if i == j == 1:
            continue
        if house[i][j] == 0:
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]  # 가로
            dp[i][j][2] = dp[i - 1][j][1] + dp[i - 1][j][2]  # 세로
            if house[i][j - 1] == house[i - 1][j] == 0:
                dp[i][j][1] = sum(dp[i - 1][j - 1])  # 대각선

print(sum(dp[-1][-1]))
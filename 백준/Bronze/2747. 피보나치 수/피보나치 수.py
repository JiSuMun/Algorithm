import sys

input = sys.stdin.readline

dp = [0] * 46


def fibo(x):
    # 종료 조건 (1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if dp[x] != 0:
        return dp[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    dp[x] = fibo(x - 1) + fibo(x - 2)
    return dp[x]


print(fibo(int(input())))
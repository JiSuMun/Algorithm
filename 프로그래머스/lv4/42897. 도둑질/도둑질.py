def solution(money):
    n = len(money)
    dp = [0]*n
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, n-1):
        dp[i] = max(dp[i-2]+money[i], dp[i-1])
    res1 = dp[-2]
    
    dp[0] = 0
    dp[1] = money[1]
    for i in range(2, n):
        dp[i] = max(dp[i-2]+money[i], dp[i-1])
    res2 = dp[-1]
    return max(res1, res2)
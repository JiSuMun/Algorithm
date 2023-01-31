import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    nums = [input().split() for _ in range(m)]
    res = 0 # 거리
    for i in range(n):
        cnt = 0
        for j in range(m-1, -1, -1): # 맨 아래 리스트부터
            if nums[j][i] == '1': res += cnt # 1 나오면 그 전에 0나왔던 cnt 만틈 res에 추가
            else: cnt += 1 # 0이 나올 때마다 카운트 추가
    print(res)
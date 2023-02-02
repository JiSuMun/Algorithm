import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
start = 0
res = 0
for i in range(1, N):
    if nums[i - 1] < nums[i]:
        res = max(res, nums[i] - nums[start])
    else:
        start = i
print(res)
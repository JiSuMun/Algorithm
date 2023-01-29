import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
l = len(nums)
sum = 0
for i in range(l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            if nums[i] + nums[j] + nums[k] > M:
                continue
            else:
                sum = max(sum, nums[i] + nums[j] + nums[k])
print(sum)
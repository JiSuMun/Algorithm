import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse = 1)
sum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            cs = nums[i] + nums[j] + nums[k]
            if cs <= M:
                if sum < cs: sum = cs
                break
print(sum)
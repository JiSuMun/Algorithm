import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
cnt = 0
w = []
for i in range(N-1):
    if nums[i] < nums[i+1]:
        cnt += (nums[i+1] - nums[i])       
    else:
        w.append(cnt)
        cnt = 0
w.append(cnt)
print(max(w))
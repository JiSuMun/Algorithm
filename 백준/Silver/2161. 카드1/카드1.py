import sys
input = sys.stdin.readline
N = int(input())
nums = list(range(1, N+1))
while len(nums) > 1:
    print(nums.pop(0), end=' ')
    nums.append(nums.pop(0))
print(nums[0])
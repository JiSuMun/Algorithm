import sys
input = sys.stdin.readline
nums = [int(input()) for _ in range(5)]
s_nums = sorted(nums)
print(sum(nums)//5, s_nums[2])
import sys
input = sys.stdin.readline
N = int(input())
n_li = list(map(int, input().split()))
M = int(input())
m_li = list(map(int, input().split()))
nums = {}
for i in n_li:
    if i in nums:
        nums[i] += 1
    else:
        nums[i] = 1
print(' '.join(str(nums[i]) if i in nums else '0' for i in m_li))
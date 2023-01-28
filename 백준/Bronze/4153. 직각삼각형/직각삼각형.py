import sys
input = sys.stdin.readline
while True:
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break
    m = max(nums)
    nums.remove(m)   
    if m**2 == nums[0]**2 + nums[1]**2:
        print('right')
    else:
        print('wrong')
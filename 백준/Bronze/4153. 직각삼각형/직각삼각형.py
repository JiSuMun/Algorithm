import sys
input = sys.stdin.readline
while True:
    nums = list(map(int, input().split()))
    n_li = sorted(nums)
    if sum(n_li) == 0: break
    elif n_li[0]**2 + n_li[1]**2 == n_li[2]**2: print('right')
    else: print('wrong')
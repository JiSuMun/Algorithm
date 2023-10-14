T = int(input())
for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    M = max(nums)
    m = min(nums)
    res = round((sum(nums) - (M + m)) / 8)
    print("#{} {}".format(t, res))
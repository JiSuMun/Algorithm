nums = list(map(int, input(). split()))

for _ in range(len(nums)):
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            print(*nums)
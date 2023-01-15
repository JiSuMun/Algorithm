N = int(input())
nums = list(map(int, input(). split()))
M = max(nums)
list = []
for i in nums:
    list.append(i/M*100)
print(sum(list)/len(list))
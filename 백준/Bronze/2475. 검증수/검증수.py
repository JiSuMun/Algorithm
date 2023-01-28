from sys import stdin
input = stdin.readline
nums = list(map(int, input().split()))
a = 0
for i in range(5):
    a += (nums[i] ** 2)
print(a % 10)
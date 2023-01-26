# 40ms
import sys
input = sys.stdin.readline
N = int(input())
nums = list(range(1, N+1))
while len(nums) > 1:
    print(nums.pop(0), end=' ')
    nums.append(nums.pop(0))
print(nums[0])

# 44ms
# def card():
#     nums = list(range(1, int(input())+1))
#     p_nums = []
#     while nums:
#         p_nums.append(nums.pop(0))
#         if nums:
#             nums.append(nums.pop(0))
#     print(*p_nums)

# if __name__ == '__main__':
#     card()
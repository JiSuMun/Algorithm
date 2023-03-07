# 48ms
"""
is_integer: 정수 여부 판단
"""
import sys
import math
input = sys.stdin.readline
n = int(input())
def four(n):
    if math.sqrt(n).is_integer(): return 1
    squares = {i**2 for i in range(1, int(math.sqrt(n)) + 1)}
    for a in squares:
        if n - a in squares: return 2
    for b in squares:
        for c in squares:
            if n - b - c in squares:
                return 3
    return 4
print(four(n))
"""
# 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다
# 자연수 n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현
# 1e9 / -1e9 : 문제에서 주어진 조건 중 수의 범위가 10억 이내일 경우 사용 가능
# """
# # 다이나믹 프로그래밍
# # 시간초과
# import sys
# import math
# input = sys.stdin.readline
# n = int(input())
# d = [0, 1]
# for i in range(2, n+1):
#     minValue = 1e9
#     for j in range(1, int(math.sqrt(i))+1):
#         minValue = min(minValue, d[i - j**2])
#     d.append(minValue + 1)
# print(d[n])
# # 브루트포스
# # 56ms
# import sys
# import math
# input = sys.stdin.readline
# def four(n):
#     # 루트n이 정수일 때
#     if int(math.sqrt(n)) == math.sqrt(n):
#         return 1
#     # 루트(n - i**2)이 정수일 때
#     for i in range(1, int(math.sqrt(n)) + 1):
#         if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):
#             return 2
#     # 루트(n - i**2 - j**2)이 정수일 때
#     for i in range(1, int(math.sqrt(n)) + 1):
#         for j in range(1, int(math.sqrt(n - i**2)) + 1):
#             if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
#                 return 3
#     return 4
# n = int(input())
# print(four(n))
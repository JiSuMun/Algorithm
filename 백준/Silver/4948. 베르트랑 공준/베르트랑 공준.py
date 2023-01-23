# 1156ms
from math import sqrt
def sosu(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

num_list = list(range(2, 246912))
prime = []

for i in num_list:
    if sosu(i):
        prime.append(i)
n = int(input())
while True:
    cnt = 0
    if n == 0:
        break
    for j in prime:
        if n < j <= 2*n:
            cnt += 1
    print(cnt)
    n = int(input())

# 1340ms
# from math import sqrt
# def Prime(n):
#     if n == 1: return False
#     for i in range(2, int(sqrt(n)+1)):
#         if n % i == 0: return False
#     return True

# num_list = list(range(2, 246912))
# prime = []

# for i in num_list:
#     if Prime(i):
#         prime.append(i)

# while True:
#     n = int(input())
#     cnt = 0
#     if n == 0: break
#     for j in prime:
#         if n < j <= 2*n:
#             cnt += 1
#     print(cnt)
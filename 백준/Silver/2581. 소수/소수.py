# 44ms
import sys
input = sys.stdin.readline
M = int(input())
N = int(input())
li = [1]*(N+1)
li[1] = 0
for i in range(2, int(N**0.5)+1):
    if li[i]:
        for j in range(i**2, N+1, i):
            li[j] = 0
li = [i for i in range(M, N+1) if li[i] == 1]
if sum(li) == 0: print(-1)
else:    
    print(sum(li))
    print(min(li))
# 56ms
# import sys
# input = sys.stdin.readline
# M = int(input())
# N = int(input())
# li = []

# for i in range(M, N+1):
#     if i == 1:
#         continue
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         li.append(i)

# if(len(li) == 0):
#     print(-1)
# else:
#     print(sum(li))
#     print(li[0])
# 544ms
# M = int(input())
# N = int(input())
# li = []
# for i in range(M, N+1):
#     c = 0
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 c += 1
#                 break
#         if c == 0:
#             li.append(i)

# if len(li) < 1:
#     print(-1)
# else:
#     print(sum(li))
#     print(min(li))
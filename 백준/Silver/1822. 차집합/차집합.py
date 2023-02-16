# 620ms
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(int, input().split()))
li = sorted([i for i in A if i not in B])
print(len(li))
if len(li) != 0: print(*li)
# 912ms, pypy: 660ms
# import sys
# input = sys.stdin.readline
# a, b = map(int, input().split())
# A = set(map(int, input().split()))
# B = set(map(int, input().split()))
# li = []
# for i in A:
#     if i not in B: li.append(i)
# print(len(li))
# if len(li) != 0: print(*sorted(li))
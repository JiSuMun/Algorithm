# 728ms, pypy3: 560ms
import sys
input = sys.stdin.readline
N = int(input())
n_li = list(map(int, input().split()))
M = int(input())
m_li = list(map(int, input().split()))
nums = {}
for i in n_li:
    if i in nums:
        nums[i] += 1
    else:
        nums[i] = 1
print(' '.join(str(nums[i]) if i in nums else '0' for i in m_li))
# 1180ms, pypy3: 728ms
# import sys
# input = sys.stdin.readline
# N = int(input())
# n_li = sorted(map(int, input().split()))
# M = int(input())
# m_li = list(map(int, input().split()))
# idx, m_dict = 0, {}
# for m in sorted(m_li): # m_li에 있는 것들만 알면 되고, n_li에 있는 모든 것들을 알 필요 없다.
#     cnt = 0
#     if m not in m_dict:
#         while idx < N:
#             if m == n_li[idx]:
#                 cnt += 1; idx += 1
#             elif m > n_li[idx]: idx += 1
#             else: break
#         m_dict[m] = cnt
# print(' '.join(str(m_dict[m]) for m in m_li))
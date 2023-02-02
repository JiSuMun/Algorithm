# 
import sys
input = sys.stdin.readline
N = int(input())
n_li = sorted(map(int, input().split()))
M = int(input())
m_li = list(map(int, input().split()))
idx, m_dict = 0, {}
for m in sorted(m_li):
    cnt = 0
    if m not in m_dict:
        while idx < N:
            if m == n_li[idx]:
                cnt += 1; idx += 1
            elif m > n_li[idx]: idx += 1
            else: break
        m_dict[m] = cnt
print(' '.join(str(m_dict[m]) for m in m_li))
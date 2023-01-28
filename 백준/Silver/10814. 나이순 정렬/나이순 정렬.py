# 264ms
# import sys
# input = sys.stdin.readline
# N = int(input())
# m_li = []
# for _ in range(N):
#     a, n = map(str, input().split())
#     a = int(a)
#     m_li.append((a, n))
# m_li.sort(key = lambda x : x[0])
# for i in m_li:
#     print(i[0], i[1])

# 112ms
import sys
m_li = sys.stdin.readlines()[1:]
m_li.sort(key = lambda x: int(x.split()[0]))
print(''.join(m_li))
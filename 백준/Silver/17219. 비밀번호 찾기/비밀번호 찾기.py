# 180ms
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
d = dict(input().rstrip().split() for _ in range(N))
res = [d[input().rstrip()] for _ in range(M)]
print('\n'.join(res))
# 시간초과
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# d = {}
# for _ in range(N):
#     a, p = input().rstrip().split()
#     d[a] = p
# for i in range(M):
#     ad = input().rstrip()
#     for k, v in d.items():
#         if ad == k: print(v)
# # 224ms
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# d = {}
# for _ in range(N):
#     a, p = input().rstrip().split()
#     d[a] = p
# for _ in range(M):
#     k = input().rstrip()
#     print(d[k])
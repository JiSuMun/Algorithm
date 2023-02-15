# 156ms
import sys
input = sys.stdin.readline
def file():
    f = {}
    N = int(input())
    for _ in range(N):
        ext = input().rstrip().split('.')[1]
        f[ext] = f.get(ext, 0) + 1
    print('\n'.join(i + ' ' + str(f[i]) for i in sorted(f.keys())))
file()
# 시간초과
# import sys
# input = sys.stdin.readline
# N = int(input())
# n_dict = {}
# f_li = sorted([input().rstrip().split('.')[1] for _ in range(N)])
# for i in range(N):
#     n_dict[f_li[i]] = f_li.count(f_li[i])
# for k, v in n_dict.items():
#     print(k, v)
# 216ms
# import sys
# input = sys.stdin.readline
# N = int(input())
# n_dict = {}
# for _ in range(N):
#     f = input().rstrip().split('.')[1]
#     if f in n_dict: n_dict[f] += 1
#     else: n_dict[f] = 1
# file = sorted(n_dict.items(), key = lambda x:x[0])
# for i in file:
#     print(i[0], i[1])
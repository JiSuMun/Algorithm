import sys
input = sys.stdin.readline
N = int(input())
n_dict = {}
for _ in range(N):
    f = input().rstrip().split('.')[1]
    if f in n_dict: n_dict[f] += 1
    else: n_dict[f] = 1
file = sorted(n_dict.items(), key = lambda x:x[0])
for i in file:
    print(i[0], i[1])
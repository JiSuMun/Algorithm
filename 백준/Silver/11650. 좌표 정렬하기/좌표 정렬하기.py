import sys
input = sys.stdin.readline
N = int(input())
n_li = []
for _ in range(N):
    a, b = map(int, input().split())
    n_li.append((a, b))
n_li = sorted(n_li)
for i in n_li:
    print(i[0], i[1])
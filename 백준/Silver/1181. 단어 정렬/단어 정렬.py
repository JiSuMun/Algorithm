import sys
input = sys.stdin.readline
N = int(input())
li = []
for _ in range(N):
    li.append(input().rstrip())
s_li = list(set(li))
ss_li = []
for i in s_li:
    ss_li.append((len(i), i))
for j, k in sorted(ss_li):
    print(k)
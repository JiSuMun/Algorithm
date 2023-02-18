import sys
input = sys.stdin.readline
N = int(input())
li = sorted(list(map(int, input().split())))
for i in range(1, N):
    li[i] += li[i-1]
print(sum(li))
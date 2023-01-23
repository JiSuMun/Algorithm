import sys
from math import sqrt
input = sys.stdin.readline
N = 123456 * 2 + 1
P = [True] * N
for i in range(2, int(sqrt(N)+1)):
    if P[i]:
        for j in range(2*i, N, i):
            P[j] = False

def prime_cnt(n):
    cnt = 0
    for i in range(n+1, n*2 + 1):
        if P[i]:
            cnt += 1
    print(cnt)

while True:
    n = int(input())
    if n == 0:
        break
    prime_cnt(n)
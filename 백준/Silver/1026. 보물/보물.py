import sys

input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

S = 0

for i in range(N):
    B_max = max(B)
    S += A[i] * B_max
    B.remove(B_max)

print(S)

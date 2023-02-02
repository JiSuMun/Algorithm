import sys
input = sys.stdin.readline
W = sorted([int(input()) for _ in range(10)], reverse = 1)
K = sorted([int(input()) for _ in range(10)], reverse = 1)
print(sum(W[:3]), sum(K[:3]))
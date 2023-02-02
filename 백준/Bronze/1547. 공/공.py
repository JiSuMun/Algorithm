import sys
input = sys.stdin.readline
M = int(input())
n = 1
for i in range(M):
	X, Y = map(int, input().split())
	if n == X: n = Y
	elif n == Y: n = X
print(n)
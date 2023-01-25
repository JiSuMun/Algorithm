import sys
input = sys.stdin.readline
N = int(input())
li = sorted([int(input()) for _ in range(N)])
print(*li, sep='\n')
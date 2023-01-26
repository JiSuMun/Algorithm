import sys
input = sys.stdin.readline
N = int(input())
PC = list(map(int, input().split()))
s = len(list(set(PC)))
print(N-s)
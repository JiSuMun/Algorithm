import sys
input = sys.stdin.readline
N = sorted(list(input().strip()), reverse=True)
for i in N:
    print(int(i), end='')
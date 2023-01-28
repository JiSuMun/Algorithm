from sys import stdin
input = stdin.readline
N = int(input())
print('\n'.join(map(str, range(1, N+1)[::-1])))
import sys
input = sys.stdin.readline
N, k = map(int, input().split())
x_li = sorted(list(map(int, input().split())), reverse = True)
print(x_li[k-1])
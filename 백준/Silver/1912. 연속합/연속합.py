import sys
si = sys.stdin.readline
n = int(si())
a = list(map(int, si().split()))
# sys.stdin = open('1912.txt', 'r').readline
# n = int(sys.stdin())
# a = list(map(int, sys.stdin().split()))

for i in range(1, n): # 0번 인덱스는 이전까지의 합이 0 자신이기 때문에 필요가 없어서 1~n 범위
    a[i] = max(a[i], a[i-1]+a[i]) # 이전까지의 모든 숫자의 합 중 최대값

print(max(a))
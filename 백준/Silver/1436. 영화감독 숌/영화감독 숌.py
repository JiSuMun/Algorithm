import sys
input = sys.stdin.readline
N = int(input())
n = 666
cnt = 0
while 1:
    if '666' in str(n):
        cnt += 1
    if cnt == N:
        print(n)
        break
    n += 1
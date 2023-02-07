import sys
input = sys.stdin.readline
N = int(input())
stack = [int(input()) for _ in range(N)] # 6 9 7 6 4 6
m = stack[-1]
res = 1 # 맨 오른쪽 막대기는 작아도 보임
for i in range(N-1, -1, -1):
    if stack[i] > m: res += 1; m = stack[i]
print(res)
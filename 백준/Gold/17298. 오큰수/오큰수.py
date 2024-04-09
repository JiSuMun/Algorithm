import sys

input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

res = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        res[stack.pop()] = arr[i]
    stack.append(i)

print(*res)

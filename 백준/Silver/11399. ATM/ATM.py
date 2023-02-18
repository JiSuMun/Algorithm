import sys
input = sys.stdin.readline
N = int(input())
li = sorted(list(map(int, input().split())))
res, ans = 0, 0
for i in li: res += i; ans += res
print(ans)
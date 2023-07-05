import sys
input = sys.stdin.readline

a = list(input().strip())
li = []
cnt = 0

for i in range(len(a)):
    if a[i] == '(': li.append(a[i])
    else:
        if a[i-1] == '(': li.pop(); cnt += len(li)
        else: li.pop(); cnt += 1

print(cnt)
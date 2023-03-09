import sys
input = sys.stdin.readline
M = int(input())
N = int(input())
li = []

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        li.append(i)

if(len(li) == 0):
    print(-1)
else:
    print(sum(li))
    print(li[0])
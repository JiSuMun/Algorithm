M = int(input())
N = int(input())
li = []
for i in range(M, N+1):
    c = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                c += 1
                break
        if c == 0:
            li.append(i)

if len(li) < 1:
    print(-1)
else:
    print(sum(li))
    print(min(li))
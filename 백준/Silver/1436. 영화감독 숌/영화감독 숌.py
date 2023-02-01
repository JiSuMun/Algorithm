import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
for i in range(9999):
    if i%1000 == 666:
        for j in range(1000):
            ans = i*1000 + j
            cnt += 1
            if n == cnt:
                break
    elif i%100 == 66:
        for j in range(100):
            ans = i*1000 + 600 + j
            cnt += 1
            if n == cnt:
                break
    elif i%10 == 6:
        for j in range(10):
            ans = i*1000 + 660 + j
            cnt += 1
            if n == cnt:
                break
    else:
        ans = i*1000 + 666
        cnt += 1
        if n == cnt:
                break
    if n == cnt:
        break
print(ans)
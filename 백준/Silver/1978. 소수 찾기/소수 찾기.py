import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
cnt = 0
for n in nums:
    c = 0
    if n == 1:
        continue
    for i in range(2, n): # 1과 자기자신을 제외한 수로 나뉘면 소수가 아님
        if n % i == 0:
            c += 1
    if c == 0:
        cnt += 1
print(cnt)

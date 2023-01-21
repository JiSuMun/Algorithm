import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
cnt = 0
for n in nums:
    
    if n == 1:
        continue
    for i in range(2, n): # 1과 자기자신을 제외한 수로 나뉘면 소수가 아님
        if n % i == 0:
            break
    else:
        cnt += 1
print(cnt)
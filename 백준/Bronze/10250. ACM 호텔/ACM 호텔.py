# YYXX: YY-층수(H), XX-번호(W)
# XX 작은 방 선호
# XX 같을 때 낮은 YY 선호
# 101-201-...-601-102-...
# 1(101)-2(201)-..-7(102)-8(202)-...

import sys
T = int(sys.stdin.readline())
for t in range(T):
    H, W, N = map(int, input().split())
    f = N % H # 손님 번호가 H넘어가면 층 = 손님수를 층수로 나눈 나머지
    cnt = (N // H) + 1 # 엘리베이터에서 떨어진 곳
    if f == 0:
        f = H
        cnt -= 1
    print(f*100+cnt)
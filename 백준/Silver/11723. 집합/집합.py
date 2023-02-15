import sys
input = sys.stdin.readline
print = sys.stdout.write
M = int(input())
s = 0
for _ in range(M):
    op, *num = input().split()
    
    if num: i = int(num[0])
    # s에 num 원소추가=> num번 비트만 1로 만들면 됨 => (1 << i)은 i번째를 1로 세팅해줌
    if op == "add": s |= (1 << i)
    # s에서 num 삭제=>num번 비트를 0으로 만들면 됨 => ~(1 << i)는 i번째 비트만 0으로 만들고 나머지는 1로 만들어줌
    elif op == "remove": s &= ~(1 << i)
    # and연산은 두 비트가 모두 1이어야 1반환한다
    elif op == "check": print('1\n' if s & (1 << i) else '0\n')
    # XOR연산은 두 비트가 서로 다를 때 1을 반환 => 토글
    elif op == "toggle": s ^= 1 << i
    # 원소채우기: 모든 비트를 0으로 만들어줌
    elif op == "all": s = (1 << 21) - 1
    # 원소 비우기
    else: s = 0 
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]
res = []
for i in range(N-7): # 8*8크기이므로 이 지점부터 8*8크기의 체스판 검사할 것
    for j in range(M-7): # i, j는 칠할 부분 찾는 시작점
        a = 0 # 시작 지점이 흰색일때
        b = 0 # 시작 지점이 검은색일때
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0: # 짝수
                    if board[k][l] != 'W': a += 1
                    else: b += 1
                else: 
                    if board[k][l] != 'W': b += 1
                    else: a += 1
        res.append(a)
        res.append(b)
print(min(res))
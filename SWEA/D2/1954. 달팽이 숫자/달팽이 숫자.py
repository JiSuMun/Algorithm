T = int(input())
for t in range(1, T+1):
    N = int(input())
    li = [[0]*N for _ in range(N)]
    s = 0
    for i in range(N//2):
        a = (N-1) - 2*i
        for j in range(a):
            li[i][i+j] = s + j+1
            li[i+j][(N-1)-i] = s + a + j+1
            li[(N-1)-i][(N-1)-(i+j)] = s + 2*a + j+1
            li[(N-1)-(i+j)][i] = s + 3*a + j+1
        s += 4*a
    if N % 2 == 1:
        li[N//2][N//2] = N**2
    print(f'#{t}')
    for k in li:
        print(*k)
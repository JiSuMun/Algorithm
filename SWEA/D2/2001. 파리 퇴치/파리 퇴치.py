T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    f = []
    # N-M+1개의 공간
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_ = 0
            for k in range(M):
                for l in range(M):
                    sum_ += board[i+k][j+l]
            f.append(sum_)   
    print(f'#{t} {max(f)}')
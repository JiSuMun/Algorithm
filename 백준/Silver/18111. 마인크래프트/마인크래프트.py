import sys
input = sys.stdin.readline
N, M, B = map(int, input().split()) # 세로, 가로, 인벤토리 블록 개수
ground = [list(map(int, input().split())) for _ in range(N)]
# sys.maxsize: 시스템이 지정할 수 있는 최댓값과 최솟값 활용 가능
# 가장 좋지 않은 방법은 큰 값을 설정할 때 9999999와 같은 임의의 값을 지정하는 것
res = sys.maxsize
height = 0 # 땅 높이
# 0~256층 반복
for g in range(257):
    ma, mi = 0, 0
    for i in range(N):
        for j in range(M):
            # 블록이 층수보다 크면
            if ground[i][j] >= g:
                ma += ground[i][j] - g
            # 블록이 층수보다 작으면
            else:
                mi += g - ground[i][j]
    # 블록을 뺀 것과 원래 있던 블록의 합이 더 커야 층을 만들 수 있음
    # 블록은 빼는 것이므로 음수로 생각하면 원래블록에서 블록빼는 값을 더하면 최하층보다 크거나 같아야 함
    if ma + B >= mi:
        # 시간을 구하고 최저 시간과 비교
        # 0~256층 비교하므로 업데이트 될수록 고층의 최저시간
        if mi + ma*2 <= res:
            res = mi + ma*2 # 최저 시간
            height = g # 층수
print(res, height)
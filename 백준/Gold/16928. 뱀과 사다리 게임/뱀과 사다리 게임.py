import sys
from collections import deque
input = sys.stdin.readline
N, M =map(int, input().split())
board = [0]*101
visited = [False]*101

l, s = {}, {} # 올라감, 내려감

for _ in range(N):
    x, y = map(int, input().split())
    l[x] = y
for _ in range(M):
    x, y = map(int, input().split())
    s[x] = y

d = deque([1])
# 덱이 빌 때까지 반복
while d:
    a = d.popleft()
    # 100번칸 가면 주사위 굴린 횟수 출력하고 break
    if a == 100:
        print(board[a])
        break
    # 주사위 1~6 하나하나 다음 위치
    for i in range(1, 7):
        next = a + i
        # 보드 벗어나지 않고, 방문하기 전이라면
        if next <= 100 and visited[next] == False:
            # 이동할 위치에 사다리
            if next in l.keys():
                next = l[next]
            # 이동할 위치에 뱀
            if next in s.keys():
                next = s[next]
            # 이동할 위치가 방문 전이라면 방문표시
            if visited[next] == False:
                visited[next] = True
                # 주사위 굴린 횟수 추가
                board[next] = board[a] + 1
                # 이동위치 덱에 삽입
                d.append(next)
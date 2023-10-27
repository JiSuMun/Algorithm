import heapq
import sys

input = sys.stdin.readline

N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]

# 강의 번호, 강의 시작 시간, 강의 종료 시간 => 시작 시간 기준 정렬
room.sort(key=lambda x: x[1])
h = []
cnt = 0
for i in room:
    # h에 값이 존재하고, 가장 일찍 끝나는 시간보다 시작 시간이 늦으면 가장 작은 값(이전 수업 값) pop
    while h and h[0] <= i[1]:
        heapq.heappop(h)
    # 힙에 끝나는 시간 추가 (다음 시작시간과 비교하기 위해)
    heapq.heappush(h, i[2])
    cnt = max(cnt, len(h))

print(cnt)

"""
dfs 시도 => 시간초과
파이썬 heapq 라이브러리 => 기본적으로 최소힙으로 구현
"""
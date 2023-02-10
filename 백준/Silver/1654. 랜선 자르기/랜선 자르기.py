import sys
input = sys.stdin.readline
K, N = map(int, input().split())
l = [int(input()) for _ in range(K)]
start, end = 1, max(l) # 이분탐색 처음과 끝위치, 가장 짧은 길이 1, 랜선 중 가장 긴 길이 end
# 모든 랜선 값을 mid로 나누어 총 몇개의 랜선이 나오나 살펴봄
while start <= end: # 적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2 # 중간 위치
    line = 0 # 랜선 수
    if sum([i//mid for i in l]) >= N: start = mid + 1
    else: end = mid -1
print(end)
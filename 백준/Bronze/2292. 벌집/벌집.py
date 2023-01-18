# 숫자가 몇 번째 육각형줄에 있는지 구하는 문제
# 6의 배수로 증가(6->12->18)
N = int(input())
n = 1 # 벌집의 개수
cnt = 1 # 1부터 카운트시작이므로
while N > n:
    n += 6 * cnt
    cnt += 1
print(cnt)
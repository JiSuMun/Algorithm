import sys
input=sys.stdin.readline
N = int(input())
for i in range(1, N+1): # 분해합 생성자 찾기
    n = sum(map(int, str(i))) # 각 자리수 더함
    n_sum = i + n # 분해합 = 생성자 + 각 자리수 합
    if n_sum == N: print(i); break # i가 작은 수부터 들어가므로 처음으로 분해합과 입력값이 같을 때 가장 작은 생성자
    elif i == N: print(0) # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 것
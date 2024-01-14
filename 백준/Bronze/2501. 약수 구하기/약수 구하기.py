import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []
for i in range(1, N+1) :
    if N % i == 0 :
        lst.append(i)

# 약수의 개수가 K보다 작을 때
if len(lst) < K :	
    print(0)
# 인덱스 번호에 맞춰서 K-1번째로 해야함
else :
    print(lst[K-1])
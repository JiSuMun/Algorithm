import sys
T = int(sys.stdin.readline())
for t in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    people = [i for i in range(1, n+1)] # 0층 1부터 n호까지의 사람수 리스트
    for j in range(k): # 층수만큼 반복
        for a in range(1, n): # 1 ~ n-1 까지 인덱스반복
            people[a] += people[a-1] # 층별 각 호 사람 수
            # print(people)
    print(people[-1]) # 마지막 인덱스 출력하면 k층 n호 거주민 수
C = int(input())

for _ in range(1, C+1):
    N_list = list(map(int, input().split()))
    average = sum(N_list[1:])/N_list[0]
    cnt = 0
    for i in N_list[1:]:
        if i > average:
            cnt += 1
    print(f'{cnt/N_list[0]*100:.3f}%')
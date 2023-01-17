# 1~99는 각 자리수 차이가 1 or 0으로 모두 한수
def hansu(n):
    h_count = 0
    for i in range(1, n+1):
        n_list = list(map(int, str(i)))
        if i < 100:
            h_count += 1
        elif n_list[0]-n_list[1] == n_list[1]-n_list[2]:
            h_count += 1
    return h_count

print(hansu(int(input())))
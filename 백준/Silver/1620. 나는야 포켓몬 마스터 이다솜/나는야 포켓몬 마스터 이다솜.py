import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 도감에 수록되어 있는 포켓몬 개수, 맞춰야하는 문제의 개수
p_dict = {}
for i in range(1, N+1):
    a = input().rstrip()
    p_dict[i] = a
    p_dict[a] = i
for _ in range(M):
    pro = input().rstrip()
    if pro.isdigit(): print(p_dict[int(pro)])
    else: print(p_dict[pro])
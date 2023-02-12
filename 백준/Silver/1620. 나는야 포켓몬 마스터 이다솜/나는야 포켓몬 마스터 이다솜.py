# 156ms
import sys
def sol():
    input = sys.stdin.readline
    N, M = map(int,input().split())
    dd = [0] + [input().strip() for i in range(N)]
    d = dict(zip(dd, range(N+1)))
    ans = [dd[int(t)] if (t:=input().strip()).isdigit() else str(d[t]) for i in range(M)]
    print("\n".join(ans))
sol()
# # python, pypy: 시간초과
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split()) # 도감에 수록되어 있는 포켓몬 개수, 맞춰야하는 문제의 개수
# p_dict = {}
# for i in range(1, N+1):
#     p_dict[i] = input().rstrip()
# m_li = [input().rstrip() for _ in range(M)]
# for i in m_li:
#     for k, v in p_dict.items():
#         if i == str(k): print(v)
#         if i == v: print(k)
# # str.isdigit(): 문자열이 숫자로만 이루어져 있는지 확인하는 함수
# # 244ms
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split()) # 도감에 수록되어 있는 포켓몬 개수, 맞춰야하는 문제의 개수
# p_dict = {}
# for i in range(1, N+1):
#     a = input().rstrip()
#     p_dict[i] = a
#     p_dict[a] = i
# for _ in range(M):
#     pro = input().rstrip()
#     if pro.isdigit(): print(p_dict[int(pro)])
#     else: print(p_dict[pro])
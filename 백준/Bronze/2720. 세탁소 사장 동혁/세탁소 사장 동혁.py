import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    C = int(input())
    m_list = []
    for i in [25, 10, 5, 1]:
        m_list.append(C//i)
        C %= i
    print(*m_list)
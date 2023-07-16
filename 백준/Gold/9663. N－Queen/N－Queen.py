import sys
input = sys.stdin.readline
N = int(input())

cnt = 0
visited = [0] * N

def is_queen(n):
    for i in range(n):
        if visited[n] == visited[i] or abs(visited[n] - visited[i]) == abs(n - i):
            return False
    
    return True

def n_queens(n):
    global cnt
    if n == N:
        cnt += 1

    else:
        for i in range(N):
            visited[n] = i
            if is_queen(n):
                n_queens(n+1)

n_queens(0)
print(cnt)
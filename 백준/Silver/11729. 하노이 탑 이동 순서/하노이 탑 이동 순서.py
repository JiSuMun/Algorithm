import sys
input = sys.stdin.readline

N = int(input())
print(2**N -1)
def hanoi(N, start, end, block):
    if N == 1: print(start, end); return
    else:
        hanoi(N-1, start, block, end); print(start, end)
        hanoi(N-1, block, end, start)

hanoi(N, 1, 3, 2)
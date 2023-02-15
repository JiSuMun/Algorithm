import sys
input = sys.stdin.readline
def file():
    f = {}
    N = int(input())
    for _ in range(N):
        ext = input().rstrip().split('.')[1]
        f[ext] = f.get(ext, 0) + 1
    print('\n'.join(i + ' ' + str(f[i]) for i in sorted(f.keys())))
file()
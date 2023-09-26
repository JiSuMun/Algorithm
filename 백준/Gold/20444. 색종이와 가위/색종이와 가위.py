import sys

input = sys.stdin.readline

n, k = map(int, input().split())
start, end = 0, n // 2 + 1


def paper(x):
    return (x + 1) * (n - x + 1)


while start != end:
    mid = (start + end) // 2
    res = paper(mid)
    if res == k:
        print("YES")
        exit(0)
    if res > k:
        end = mid
    else:
        start = mid + 1

print("NO")
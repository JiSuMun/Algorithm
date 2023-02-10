import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)
while start <= end:
    c_tree = 0
    mid = (start + end) // 2
    for i in tree:
        if i >= mid: c_tree += i - mid
    if c_tree >= M: start = mid + 1
    else: end = mid -1
print(end)
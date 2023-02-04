import sys
input = sys.stdin.readline
li = []
for _ in range(int(input())):
    li.append(list(map(int, input().split())))
li = sorted(li, key = lambda x:(x[1], x[0]))
for i in li:
    print(i[0], i[1])
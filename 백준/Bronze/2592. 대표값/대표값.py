import sys
input = sys.stdin.readline
n_li = [int(input()) for _ in range(10)]
cnt = [n_li.count(n) for n in n_li]
print(sum(n_li)//10, n_li[cnt.index(max(cnt))], sep = '\n')
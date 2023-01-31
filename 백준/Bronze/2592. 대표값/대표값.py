import sys
from collections import Counter
input = sys.stdin.readline
n_li = [int(input()) for _ in range(10)]
print(sum(n_li)//10, Counter(n_li).most_common(1)[0][0], sep ='\n')
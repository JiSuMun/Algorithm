import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
li = []
for i in range(N):
    li.append(input().strip())
li.sort()    
new = Counter(li).most_common()
print(new[0][0])
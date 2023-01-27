import sys
from collections import deque
input = sys.stdin.readline
li = deque()
while 1:
    s = input().rstrip()
    if s == '고무오리 디버깅 시작': continue
    if s == '고무오리 디버깅 끝': break
    if s == '문제': li.append(s)
    elif s == '고무오리':
        if len(li) == 0:
            li.append('문제')
            li.append('문제')
        else:
            li.pop()
if li:
    print('힝구')
else:
    print('고무오리야 사랑해')
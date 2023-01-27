# 60ms
# import sys
# from collections import deque
# input = sys.stdin.readline
# li = deque()
# while 1:
#     s = input().rstrip()
#     if s == '고무오리 디버깅 시작': continue
#     if s == '고무오리 디버깅 끝': break
#     if s == '문제': li.append(s)
#     elif s == '고무오리':
#         if len(li) == 0:
#             li.append('문제')
#             li.append('문제')
#         else:
#             li.pop()
# if li:
#     print('힝구')
# else:
#     print('고무오리야 사랑해')

# 44ms
import sys
input = sys.stdin.readline
cnt = 0
while 1:
    s = input().rstrip()
    if s == '고무오리 디버깅 끝': break
    else:
        if s == '문제': cnt += 1
        elif s == '고무오리':
            if cnt <= 0:
                cnt += 2
            else: cnt -= 1
if cnt == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')
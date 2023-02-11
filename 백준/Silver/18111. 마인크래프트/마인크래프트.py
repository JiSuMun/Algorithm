from sys import stdin
from collections import Counter
n, m, b = map(int, stdin.readline().split())
arr = stdin.readlines()
ground = []
for row in arr:
    ground += list(map(int, row.split()))
c = Counter(ground)
to_inventory = sum(k*v for k, v in c.items()) # 인벤토리에 넣을 블록
need_block = 0 # 인벤토리에서 꺼내는 블록
need_cur_floor = c[0]
nm = n*m # 블록 면적 개수
min_time = 2*to_inventory # 최대 시간 저장
max_h = 0
for h in range(1, 257):
    need_block += need_cur_floor
    to_inventory -= nm - need_cur_floor
    need_cur_floor += c[h]
    if to_inventory + b < need_block:
        break
    if 2*to_inventory + need_block <= min_time:
        min_time = 2*to_inventory + need_block # 최저 시간
        max_h = h
print(min_time, max_h)
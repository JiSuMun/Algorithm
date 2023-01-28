from sys import stdin
input = stdin.readline
s_list = list(input().split())
if s_list == sorted(s_list): print('ascending')
elif s_list == sorted(s_list, reverse = 1): print('descending')
else: print('mixed')
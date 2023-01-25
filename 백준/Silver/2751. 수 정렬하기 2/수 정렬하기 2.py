# python3 => 1340ms, pypy3 => 
# import sys
# input = sys.stdin.readline
# N = int(input())
# li = sorted([int(input()) for _ in range(N)])
# print(*li, sep='\n')

# pypy3 => 464ms
from sys import stdin
n = int(stdin.readline())

nums = sorted(map(int, stdin.read().split())) # read(): 파일 전체의 내용을 하나의 문자열로 읽어옴
print('\n'.join(map(str, nums))) # join은 리스트와 써야 하므로 map사용
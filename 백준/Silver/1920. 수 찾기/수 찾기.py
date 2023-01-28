import sys
input = sys.stdin.readline
N = int(input())
A = set(map(int, input().split())) # set은 탐색 시간복잡도가 상수
M = int(input())
B = list(map(int, input().split()))
sys.stdout.write('\n'.join('1' if i in A else '0' for i in B))
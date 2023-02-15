import sys
input = sys.stdin.readline
for _ in range(int(input())):
    # RR은 안 뒤집는것과 동일하므로 지워주기
    # R 앞뒤로 있는 D의 개수
    p_list = list(map(len, input().rstrip().replace('RR','').split('R')))
    # RDD => [0, 2], DD => [2], RRD => [1], D => [1]
    n = int(input())
    n_list = input().rstrip()[1:-1].split(',')   
    # RDD => 0 2, DD => 2 1, RRD => 1 6, D => 1 0
    lo, hi = sum(p_list[::2]), n - sum(p_list[1::2]) 
    # R 앞에 있는 D 개수, 총 개수 - R뒤에 있는 D개수
    if lo <= hi:
        print_list = n_list[lo:hi] if len(p_list)%2 else n_list[lo:hi][::-1]
        print('[' + ','.join(print_list) + ']')
    else:
        print('error')
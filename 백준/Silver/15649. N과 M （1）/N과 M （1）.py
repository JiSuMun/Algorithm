import sys
input = sys.stdin.readline
N, M = map(int, input().split())
li = [] # M개의 수열을 저장하기 위한 리스트
def s_15649():
    if len(li) == M: # M개가 되면 출력하고 함수 끝
        print(' '.join(map(str, li)))
        return
    for i in range(1, N+1): # 1~N
        if i not in li: # 리스트와 중복 확인
            li.append(i) 
            s_15649()
            li.pop() # 4 2 입력이라면 1 - 1,2 - 1 - 1,3 - 1 - 1,4
s_15649()
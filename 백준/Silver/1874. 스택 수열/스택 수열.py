import sys
input = sys.stdin.readline
n = int(input())
stack = []
res = [] # +, - 결과
# 1이상 n이하 정수가 하나씩 주어진다고 했고
# 아래 반복문에서 오름차순이면 cnt += 1을 하면서 cnt를 stack에 저장중이므로 cnt = 1부터 시작
cnt = 1 
flag = True
for i in range(n):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while cnt <= num:
        stack.append(cnt)
        res.append('+')
        cnt += 1
    # num과 stack 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        res.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        flag = False
        break
if flag == False: print('NO')
else: print(*res, sep = '\n')
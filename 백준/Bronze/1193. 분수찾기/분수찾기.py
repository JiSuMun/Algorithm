# 대각선 라인 기준 지그재그이므로
# 홀수 라인: 갈수록 분자-1, 분모+1
# 짝수 라인: 갈수록 분자+1, 분모-1
# 분모 개수가 n라인에 n개 존재
X = int(input()) # X번째 분수 구하기
line = 1 # 라인은 1/1의 1줄부터 시작이다.

while X > line: # X가 대각선 line 수보다 작아질 때, 해당 대각선에 X가 있다.
    X -= line # line에서 X가 몇번째 위치하는지 알 수 있다.
    line += 1

if line % 2 == 0:
    up = X
    down = line - X + 1
else:
    up = line - X + 1
    down = X
print(f'{up}/{down}')
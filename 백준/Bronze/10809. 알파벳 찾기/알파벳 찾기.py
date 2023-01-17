S = input()
for s in range(97, 123):
    print(S.find(chr(s)), end=' ') # find 함수는 문자열에서만 사용 가능, 찾는 문자가 문자열 안에 포함되지 않은 경우 -1을 출력
S = input().upper()
s_list = list(set(S))

cnt = []
for i in s_list:
    cnt.append(S.count(i)) # 입력받은 문자열의 알파벳 개수를 추가

if cnt.count(max(cnt)) > 1: # cnt 리스트에서 가장 높은 숫자가 2개 이상일 때
    print('?')

else:
    print(s_list[cnt.index(max(cnt))]) # cnt 리스트에서 가장 높은 숫자의 인덱스 번호를 찾아서 s_list에서 알파벳 출력
# 각 숫자의 자리수가 다르기 때문에 오류 발생
# 때문에 숫자들의 자릿수를 맞춰줘야 하고, 조건에 원소가 0이상 1000이하라고 되어있으므로
# 숫자를 3으로 곱하면 숫자자체가 달라지기 때문에
# 문자로 바꿔 *3해서 비교한다.
def solution(numbers):
    # if sum(numbers) == 0: return '0'
    numbers = list(map(str, numbers)) # 문자열 리스트로 만들어줌
    numbers.sort(key = lambda x:x*3, reverse = True)
    return str(int(''.join(numbers)))
x_list = []
y_list = []
res_x = 0
res_y = 0

for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for x, y in zip(x_list, y_list): # 여러개의 오브젝트나 리스트 등을 for문에서 동시에 사용하고 싶은 경우에는 zip함수 사용
    if x_list.count(x) == 1:
        res_x = x
    if y_list.count(y) == 1:
        res_y = y

print(res_x, res_y)
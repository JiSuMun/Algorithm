n_list = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        n_list.append(num)
if n_list:
    print(sum(n_list), min(n_list), sep='\n')
else:
    print(-1)
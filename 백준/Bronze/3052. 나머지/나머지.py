list = []
for _ in range(1, 11):
    n = int(input())
    list.append(n%42)
print(len(set(list)))
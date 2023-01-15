list = [i for i in range(1, 31)]

for _ in range(1, 29):
    n = int(input())
    list.remove(n)
print(min(list))
print(max(list))
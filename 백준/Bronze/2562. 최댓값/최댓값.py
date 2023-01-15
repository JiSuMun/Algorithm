list = []
for t in range(1, 10):
    n = int(input())
    list.append(n)
a= max(list)
print(a)
print(list.index(a)+1)
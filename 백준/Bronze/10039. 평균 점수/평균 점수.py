list = []
for i in range(5):
    n = int(input())
    if n < 40:
        n = 40
    list.append(n)
print(round(sum(list)/len(list)))
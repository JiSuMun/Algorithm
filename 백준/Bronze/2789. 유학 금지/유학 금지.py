str = list(input())

S = list('CAMBRIDGE')
s_list = []
for i in str:
    if i not in S:
        s_list.append(i)
print(*s_list, sep = '')
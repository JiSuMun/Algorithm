C = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()
for i in C:
    str = str.replace(i, 'C')
print(len(str))
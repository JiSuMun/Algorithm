dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
al = input()
time = 0

for i in al:
    for j in dial:
        if i in j:
            time += dial.index(j) + 3
print(time)
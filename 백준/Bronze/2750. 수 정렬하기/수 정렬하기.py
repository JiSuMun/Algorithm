N = int(input())
n_list = []
for n in range(1, N+1):
    n = int(input())
    n_list.append(n)
print(*sorted(n_list), sep='\n')
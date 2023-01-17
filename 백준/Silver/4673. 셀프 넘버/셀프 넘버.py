def d(n):
    n += sum(map(int, str(n)))
    return n
nums = set()

for i in range(1, 10001):
    nums.add(d(i))

for j in range(1, 10001):
    if j not in nums:
        print(j)
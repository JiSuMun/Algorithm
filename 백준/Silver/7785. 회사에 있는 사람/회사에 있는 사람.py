import sys
n = int(sys.stdin.readline())
people = {}
for _ in range(n):
    name, status = sys.stdin.readline().split()
    people[name] = status
    if status == 'leave':
        del people[name]
P = dict(sorted(people.items(), reverse = 1))
for key in P.keys():
    print(key)
import sys
input = sys.stdin.readline
angle = [int(input()) for _ in range(3)]
result = 0
if sum(angle) == 180:
    for i in angle:
        if angle.count(i) == 3:
            result = 'Equilateral'
        elif angle.count(i) == 2:
            result = 'Isosceles'
        elif angle.count(i) == 1:
            result = 'Scalene'
    print(result)
else:
    print('Error')
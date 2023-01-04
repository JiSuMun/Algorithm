a, b, c = map(int, input().split())
result = 0

if a==b==c:
    result = 10000+a*1000
    print(result)
elif a==b or c==a:
    result = 1000+a*100
    print(result)
elif b==c:
    result = 1000+b*100
    print(result)
elif a != b != c:
    result = max(a, b, c)*100
    print(result)
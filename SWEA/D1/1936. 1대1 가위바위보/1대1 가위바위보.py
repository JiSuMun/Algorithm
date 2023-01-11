a, b = map(int, input().split())

if a-b == 2 or a-b==-1: # B가 이기는 경우: 가위(A 보)=> , 바위(A 가위), 보(A 바위)
    print("B")
else:
    print("A")
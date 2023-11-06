T = int(input())
for t in range(1, T + 1):
    n = int(input())
    s = input()
    if len(s) % 2 != 0:
        res = "No"
    else:
        if s[: len(s) // 2] == s[len(s) // 2 :]:
            res = "Yes"
        else:
            res = "No"
    print(f"#{t} {res}")
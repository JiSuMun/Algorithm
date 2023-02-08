from sys import stdin

def sol2108():
    n = int(stdin.readline()) # 숫자개수
    # 입력받는 수는 -4000~4000까지 정수이므로 리스트만들어서 각각의 정수가 몇 개 포함되어 있는지 센다
    counts = [0]*8001 
    s = 0 # 합
    for i in stdin:
        num = int(i)
        # 모든 수를 0이상으로 만들어 리스트에 저장
        counts[num+4000] += 1

    maxc = max(counts) # 가장 큰 수
    mode = mcnt = 0 # 최빈값
    idx = 0
    med = None # 중앙값
    mi, ma = 4001, -4001 
    for i in range(8001):
        cnt = counts[i]
        if cnt == 0:
            continue

        num = i-4000 # 원래 수로 돌림
        s += num*counts[i]
        if cnt == maxc and mcnt < 2:
            mode = num
            mcnt += 1
        mi = min(mi, num) # 최소값
        ma = max(ma, num) # 최대값
        idx += counts[i]
        if idx >= n//2+1 and med == None:
            med = num

    print(round(s/n), med, mode, ma-mi, sep='\n')

if __name__ == '__main__':
    sol2108()
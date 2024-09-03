path = []


# 주사위 몇 개 던졌는지, 주사위의 합이 몇 인지?
def recur(level, total) :
    # 가지치기 : 이미 10을 넘는 경우의 수는 계산할 필요가 없다!
    if total > 10 :
        return
    
    # 기저 조건 : 3개를 던졌을 때 종료
    if level == 3:
        # 10 이하
        if total <= 10 :
            print(path)

        return

    # 후보군 탐색
    for i in range(1, 7)  :
        path.append(i)
        recur(level + 1, total + i)
        path.pop()
recur(0, 0)
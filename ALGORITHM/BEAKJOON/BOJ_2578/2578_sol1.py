# main
Bingo = [list(map(int,input().split())) for _  in range (5)]
call_2d =  [list(map(int,input().split())) for _  in range (5)]

call = [element for row in call_2d for element in row]
check_k = [0] * 5
check_t = [0] * 5
cnt = 0         # 몇 번째인지
cross_check = 0
re_cross_check = 0
Bingo_check = 0  # Bingo_check를 외부에서 초기화
# call도 돌고 Bingo도 돌아
for i in range (len(call)) :   # call 돌아
    for k in range(len(Bingo)) : # Bingo안에서 찾아
        for t in range(len(Bingo)) :
            if Bingo[k][t] == call[i] :
                check_k[k] += 1
                check_t[t] += 1
                cnt += 1
                if k == t :
                    cross_check += 1

                if t == 4 - k :
                    re_cross_check += 1

    if cnt > 10 :       # 1번 정도는 번호를 불러야지
        Bingo_check = 0
        for r in range (5) :    # k, t 다 돌리기
            if check_k[r] == 5 : # 행 빙고
                Bingo_check += 1
                check_k[r] = -1     # 빙고 된거는 체크 X
            if check_t[r] == 5 : # 열 빙고
                Bingo_check += 1
                check_t[r] = -1
        if cross_check == 5 :
            Bingo_check += 1
            cross_check = -1
        if re_cross_check ==5 :
            Bingo_check += 1
            re_cross_check = -1

    if Bingo_check >= 3 :
        print(call[i])
        break


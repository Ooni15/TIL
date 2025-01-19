def total_cnt():

    cnt = 0
    for i in range(3):
        for j in range(5):

            if check_arr[i][j] == 5:
                cnt += 1

    return cnt



Bingo = [list(map(int,input().split())) for _ in range(5)]
call = [list(map(int,input().split())) for _ in range(5)]

# 저장하는 배열
check_arr = [[0] * 5 for _ in  range(3)]    # 1행 행, 2행 열 , 3행 대각선
# 방문 배열
visited = [[False] * 5 for _ in range(5)]
result = 0
found = False
for i in range(5):
    for j in range(5):
        now = call[i][j]
        if found == True:
            break
        result += 1
        for k in range(5):
            for t in range(5):

                if visited[k][t]:
                    continue

                if now == Bingo[k][t]:
                    visited[k][t] = True
                    check_arr[0][k] += 1    # 행 체크
                    check_arr[1][t] += 1    # 열 체크

                    # 대각선 체크
                    if k == t :
                        check_arr[2][0] += 1
                        if k == 2:
                            check_arr[2][1] += 1
                    elif (k == 4 and t == 0) or (k ==3 and t == 1) or (k == 1 and t == 3) or (k == 0 and t == 4):
                        check_arr[2][1] += 1

        bingo_cnt = total_cnt()

        if bingo_cnt >= 3:
            print(result)
            found = True
            break


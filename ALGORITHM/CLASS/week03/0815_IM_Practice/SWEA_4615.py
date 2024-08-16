T = int(input())

for test_case in range (1, T + 1) :
    N = int(input())
    arr = [list(map(str,input())) for _ in range (N)]

    for i in range (N) :
        for j in range (N) :
            if arr[i][j] == '.' :
                arr[i][j] = 0
            else :
                arr[i][j] = 1

    # 가로췤
    check = 0
    result = 'No'
    for i in range (N) :
        cnt = 0
        for j in range (N) :
            sum_1, sum_2, sum_3 ,sum_4= 0, 0, 0, 0
            if j + 5 < N + 1:
                #print(1111111111)
                for k in range (5) :
                    sum_1 += arr[i][j + k]   # 가로
                    # sum1 += arr[i + k][j + k]
                    sum_2 += arr[j + k][i]   # 세로
                    # sum3 += arr[i + k][j + k]

                if sum_1 == 5 or sum_2 == 5 :
                    result = 'YES'
                    check = 1
                    break
                else:
                    result = 'NO'

            if i + 5 < N + 1 and j + 5 < N  + 1:          # 범위 재확인 필요
                for k in range(5) :
                    t = j + k
                    #print(N - t -1)
                    sum_3 += arr[i + k][j  + k ]        # 대각선
                    sum_4 += arr[i + k][N - t - 1]      # 반대 대각선
                    #print(cnt)
                    #print(sum_4)
                if sum_3 == 5 or sum_4 == 5 :
                    result = 'YES'
                    check = 1
                    break
                else :
                    result = 'NO'
        if check == 1 :
            break
            # if sum1 == 5 or sum2 == 5 or sum3 == 5 or sum4 == 5 or sum_test == 5:
            #     result = 'YES'
            #     break
            # else :
            #     result = 'NO'

    print(f'#{test_case}',result)
"""
1
5
....o
...o.
..o..
.o...
o....
"""

import sys
sys.stdin = open("input (5).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    for i in range (9) :
        cnt_row = 0
        lst_row = arr[i][:]
        lst_row.sort()
        #print(i , lst_row)

        if lst_row != list(range(1,10)) :
            result = 0
            break
        else :
            result = 1

        # 열
        lst_column = [row[i] for row in arr]
        lst_column.sort()
        #print(lst_column)
        if lst_column != list(range(1,10)) :
            result = 0
            break
        else :
            result = 1


        for i in range(0, 9 , 3) :
            for j in range(0, 9, 3) :
                lst_box = []
                for x in range(3) :
                    for y in range(3) :
                        lst_box.append(arr[i+x][j+y])

            lst_box.sort()
            #print(lst_box)
            if lst_box != list(range(1,10)) :
                result = 0
                break
            else :
                result = 1


    print(f'#{test_case} {result}')

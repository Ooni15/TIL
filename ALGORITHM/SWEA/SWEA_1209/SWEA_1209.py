import sys
sys.stdin = open("input (4).txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_max = 0
    index = 0
    for i in range (100) :
        sum_row = 0
        sum_column = 0
        sum_right = 0
        sum_left = 0
        for j in range (100) :
            # 행 합
            sum_row += arr[i][j]
            if sum_max < sum_row :
                sum_max = sum_row

            # 열 합
            sum_column += arr[j][i]
            if sum_max < sum_column :
                sum_max = sum_column

            # 좌측 대각선

            sum_left += arr[j][j]
            if sum_max < sum_left :
                sum_max = sum_left

            # 우측 대각선

            sum_right += arr[j][100 - 1 - j]
            if sum_max < sum_right :
                sum_max = sum_right

    print(f'#{test}',sum_max)

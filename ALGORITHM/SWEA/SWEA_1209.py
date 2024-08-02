# 최댓값 구하기
def mani(arr):
    max_num = 0  # 1-9 중 작은값
    # 최대값 구하기
    for i in range(len(arr)):
        if max_num < arr[i]:
            max_num = arr[i]

    return max_num

# 합 구하기
def plus(arr):
    sum_num = 0
    for i in range(len(arr)):
        sum_num += arr[i]

    return sum_num

T = 10

for test_case in range (1, T+1) :
    tc = int(input())
    N = 100
    numbers = [list(map(int,input().split())) for _ in range (N)]   # 100 X 100 행렬


    # main
    column, cross1, cross2, row_sum, column_sum = [0] * N, [0] * N, [0] * N, [0] * N, [0] * N
    for i in range (N) :
        # row : 한 행의 합을 sum 배열에 저장
        row_sum[i] = plus(numbers[i])
        # cross1 : 왼쪽 대각 값 cross1 배열에 저장
        cross1[i] = numbers[i][i]
        # cross 2 : 오른쪽 대각 값 cross2 배열에 저장
        cross2[i] = numbers[i][N - 1 - i]

        for j in range(N) :
            # column : 열의 값 column 배열에 저장
            column[j] = numbers[j][i]

        # 각 열의 합 column_sum 배열에 저장
        column_sum[i] = plus(column)

    # row의 최댓값
    row_max = mani(row_sum)
    # column의 최댓값
    column_max = mani(column_sum)
    # cross1 배열의 합
    cross1_max = plus(cross1)
    # cross2 배열의 합
    cross2_max = plus(cross2)

    # 4가지 값 중 최댓값
    result = mani([row_max, column_max, cross1_max, cross2_max])

    print(f'#{test_case} {result}')
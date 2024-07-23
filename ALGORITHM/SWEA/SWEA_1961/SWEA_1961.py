T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    def rotation(arr):

        rotated = [[0] * N for _ in range(N)]


        for i in range(N):
            for j in range(N):
                rotated[i][j] = arr[(N - 1 - j)][i]

        return rotated

    arr_90 = rotation(arr)
    arr_180 = rotation(arr_90)
    arr_270 = rotation(arr_180)

    print(f'#{test_case}')
    for i in range (N) :
        print(''.join(map(str, arr_90[i])), end=' ')
        print(''.join(map(str, arr_180[i])), end=' ')
        print(''.join(map(str, arr_270[i])), end='\n')


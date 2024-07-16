import sys
sys.stdin = open("in1.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr = [[0] * (N + 2 * M) for _ in range(M)] + \
          [[0] * M + list(map(int, input().split())) + [0] * M for _ in range(N)] + \
          [[0] * (N + 2 * M) for _ in range(M)]

    print(arr)

    sum_max = 0
    sum_max_p = 0
    sum_max_m = 0

    for i in range (M, N+M) :
        for j in range (M, N+M) :
            sum_baby_p = arr[i][j]
            sum_baby_m = arr[i][j]
            for k in range (1,M) :
                sum_baby_p += arr[i][j - k]
                sum_baby_p += arr[i][j + k]
                sum_baby_p += arr[i - k][j]
                sum_baby_p += arr[i + k][j]

                if sum_max < sum_baby_p:
                    sum_max = sum_baby_p

            for t in range (1,M) :
                sum_baby_m += arr[i - t][j - t]
                sum_baby_m += arr[i + t][j + t]
                sum_baby_m += arr[i + t][j - t]
                sum_baby_m += arr[i - t][j + t]

                if sum_max < sum_baby_m :
                    sum_max = sum_baby_m


    print(f'#{test_case} {sum_max}')
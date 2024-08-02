T = int(input())

for test_case in range(1, 1+T) :

    N = int(input())

    arr = [list(map(int,input())) for _ in range(N)]
    t = (N//2) + 1 # 3
    i = 0
    total = 0
    while i > -1 :
        for j in range(t) :
            total += arr[(N // 2) + i][(N // 2) - j]
            total += arr[(N // 2) + i][(N // 2) + j]
            total += arr[(N // 2) - i][(N // 2) - j]
            total += arr[(N // 2) - i][(N // 2) + j]

        i += 1
        t -= 1
        if t == 0 :
            break

    check = 0

    for k in range(N) :
        check += arr[k][N//2]

    check += sum(arr[N//2])
    result = total - check - (arr[N//2][N//2])
    print(f'#{test_case} {result}')
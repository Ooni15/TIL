T = int(input())

for test_case in range (1,T+1) :

    M, N = map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range (M)]

    total_max = 0
    cnt = 0
    for i in range(M - N + 1) :
        for j in range(M - N + 1) :
            total = 0
            for k in range(N) :
                for t in range(N) :
                    total += arr[i + k][j + t]
                    cnt += 1
                if total_max < total :
                    total_max = total

    print(f'#{test_case} {total_max}')
    
T = int(input())

for test_case in range (1, T + 1) :
    N = int(input())
    arr = list(map(int,input().split()))
    max_cnt, cnt = 1, 1
    for i in range (N) :
        if i + 1 < N :
            if arr[i] < arr [i + 1] :
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
            else :
                cnt = 1



    print(f'#{test_case}', max_cnt)
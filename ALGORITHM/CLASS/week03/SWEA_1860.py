T = int(input())

for test_case in range (1, T + 1) :

    N, M, K = map(int,input().split())
    arrive = list(map(int,input().split()))
    arrive.sort()
    #print(arrive)
    # total_lst = [0] * (sum(arrive) + 1)
    #
    #
    # count = sum(arrive) // M
    cnt = 0
    for i in range(0, max(arrive) + 1) :

        if i!= 0 and i % M == 0 and i in arrive :
            cnt -= 1
            cnt += K
        elif i != 0 and i % M == 0 :
            cnt += K
        elif i in arrive :
            cnt -= 1
        else :
            cnt += 0

        #print(i, cnt)
        if cnt < 0 :
            result = 'Impossible'
            break
        else:
            result = 'Possible'



    # # 구운 붕빵 먼저 넣어버려! (시간 인덱스와 동일하게)
    # for i in range(1, count + 1) :
    #     total_lst[M  * i] += K          # 구운 거 넣어!

    # 붕빵 가져가버려!
    # for i in range(N):
    #
    #     total_lst[arrive[i]] = sum(total_lst[:arrive[i] + 1]) - 1  # 붕어빵 가져가고 남은 붕빵 적어놔!
    #     if total_lst[arrive[i]] < 0 :
    #         result = 'Impossilble'
    #         break
    #     else :
    #         result = 'Possible'



    print(f'#{test_case}', result)



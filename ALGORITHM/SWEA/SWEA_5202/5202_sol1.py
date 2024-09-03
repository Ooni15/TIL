T = int(input())

for test_case in range (1, T + 1) :

    N = int(input())
    time_lst = [0] * N

    for i in range (N) :
        s, e = map(int,input().split())
        time_lst[i] = [e,s]

    time_lst.sort()
    visited = [False] * N
    cnt = 1

    for i in range(N) :
        if not visited[i]:
            for j in range(i + 1, N) :
                a = time_lst[i][0]
                b = time_lst[j][1]
                if time_lst[i][0] > time_lst[j][1] :
                    visited[j] = True
                elif not visited[j] and time_lst[i][0] <= time_lst[j][1] :
                    cnt += 1
                    break

    print(f'#{test_case} {cnt}')


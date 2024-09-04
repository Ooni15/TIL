T= int(input())

for test_case in range(1,T + 1) :

    N , M = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range (N)]

    di = [ 0, 0, 1, 0, -1]
    dj = [ 0, 1, 0, -1, 0]

    max_total = 0

    for i in range (N) :
        for j in range (M) :
            total = 0
            for k in range (5) :
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0<= nj < M:
                    total += lst[ni][nj]
            if max_total < total :
                max_total = total

    print(f'#{test_case} {max_total}')
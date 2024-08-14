# 델타 함수 만들기
def dx_dy(K) :

    # 기본 상하좌우 델타 값
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    new_dx = []
    new_dy = []
    for i in range (1, K + 1) :     # K배 해주기
        for j in range (len(dx)) :
            new_dx.append(dx[j] * i)
            new_dy.append(dy[j] * i)

    # 자기 자신 추가하기
    new_dx.append(0)
    new_dy.append(0)
    return new_dx, new_dy



T = int(input())

for test_case in range (1, T + 1) :

    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range (N)]


    max_sum = 0
    for i in range (N) :
        for j in range (M) :
            sum = 0
            dx, dy = dx_dy(arr[i][j])
            # print('dx', dx)
            # print('dy', dy)
            for k in range (len(dx)) :
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < M :
                    sum += arr[ni][nj]
                    if max_sum < sum :
                        max_sum = sum


    print(f'#{test_case}', max_sum)


# 움직이기
def move_ball(ball_arr):

    L = len(ball_arr)

    for i in range(L):
        r, c, m, s, d = ball_arr[i][0] -1 , ball_arr[i][1] - 1, ball_arr[i][2], ball_arr[i][3], ball_arr[i][4]
        nr = ((r + (s%N)*dr[d] + N) % N) + 1
        nc = ((c + (s%N)*dc[d] + N) % N) + 1

        check_location[nr][nc].append([nr, nc, m, s, d])
        check_m[nr][nc] += m
        check_s[nr][nc] += s

# 합치기
def new_ball(location):

    new_fireball = []

    for i in range(1, N+1):
        for j in range(1, N+1):
            if len(location[i][j]) == 0:
                continue
            elif len(location[i][j]) >=2:
                even_cnt, odd_cnt = 0, 0
                y, x = location[i][j][0][0], location[i][j][0][1]
                for k in range(len(location[i][j])) :
                    d = location[i][j][k][4]
                    if d % 2 == 0:
                        even_cnt += 1
                    else :
                        odd_cnt += 1

                # 계산하자
                m = check_m[y][x] // 5
                # print(m)
                if m == 0 :
                    continue

                s = check_s[y][x] // len(location[i][j])

                if odd_cnt == 0 or even_cnt == 0:
                    for t in range(4):
                        new_fireball.append([y, x, m, s, 2*t])
                else :
                    for t in range(4):
                        new_fireball.append([y, x, m, s, 2*t + 1])

            elif len(location[i][j]) == 1:
                new_fireball.append(location[i][j][0])

    # print('위에',new_fireball)
    return new_fireball


N, M, K = map(int,input().split())      # 네모크기, 파이어볼 개수, 이동 횟수
fireball = [list(map(int,input().split())) for _ in range(M)]
# r, c, m, s, d     # 행, 열, 질량, 속력, 방향

# 방향 받기
# [0, 1, 2, 3, 4, 5, 6, 7]
# [위, 우위대, 우, 우아대, 아래, 왼아대, 왼, 왼위대]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
dr = [-1, -1, 0, 1, 1, 1, 0,-1]

# K번 움직일 거임
for i in range(K):
    check_location = [[[] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    check_m = [[0] * (N + 1) for _ in range(N + 1)]
    check_s = [[0] * (N + 1) for _ in range(N + 1)]

    # 공 움직이기!
    moveball = move_ball(fireball)
    # print(check_m)
    # print(check_location)

    fireball = new_ball(check_location)

    # print('밑에', fireball)

result = 0
for i in range(len(fireball)):
    result += fireball[i][2]

print(result)
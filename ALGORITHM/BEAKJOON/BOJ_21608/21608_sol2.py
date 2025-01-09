N = 3  # 크기
arr = [
    [4, 2, 5, 1, 7],
    [3, 1, 9, 4, 5],
    [9, 8, 1, 2, 3],
    [8, 1, 9, 3, 4],
    [7, 2, 3, 4, 8],
    [1, 9, 2, 5, 7],
    [6, 5, 2, 3, 4],
    [5, 1, 9, 2, 8],
    [2, 9, 3, 1, 4]
]

num = [0] * (N ** 2)
friends = [0] * (N ** 2)
result = 0  # 최종 결과 점수
count_arr = [0] * (N ** 2 + 1)  # 학생 번호를 순서대로 기록하는 배열

# 각 학생의 번호와 친구들 저장
for i in range(N ** 2):
    num[i] = arr[i][0]
    friends[i] = arr[i][1:]

# 좌석 배열 초기화 (-1로)
new_seat = [[-1] * N for _ in range(N)]

# 상하좌우 탐색용
dx = [0, 0, -1, 1]  # 상, 하, 좌, 우
dy = [-1, 1, 0, 0]

# 학생 배치 과정
for i in range(N ** 2):
    my_num = num[i]
    my_friends = friends[i]

    bf_max = 0  # 친구 수
    empty_max = 0  # 빈자리 수
    now_x, now_y = -1, -1

    # 내 주변 옆자리 확인하기
    for k in range(N):
        for t in range(N):
            bf = 0  # 친구 수
            empty = 0  # 빈자리 수
            seat = new_seat[k][t]

            # 이미 앉은 자리가 있으면 넘어가
            if seat != -1:
                continue

            # 주변 4방향 탐색
            for n in range(4):
                y = k + dy[n]
                x = t + dx[n]

                if x < 0 or x >= N or y < 0 or y >= N:
                    continue

                if new_seat[y][x] == -1:  # 빈 자리
                    empty += 1
                elif new_seat[y][x] in my_friends:  # 친구가 앉아 있음
                    bf += 1

            # 친구가 많은 자리 우선, 친구 수 같으면 빈자리 수 많은 자리
            if bf_max < bf:
                bf_max = bf
                empty_max = empty
                now_y, now_x = k, t
            elif bf_max == bf:
                if empty_max < empty:
                    empty_max = empty
                    now_y, now_x = k, t

    # 찾은 자리 배치
    new_seat[now_y][now_x] = my_num

print(new_seat)
# 배치 완료 후 점수 계산
for i in range(N):
    for j in range(N):
        result_bf = 0
        last_friends = friends[num.index(new_seat[i][j])]  # 해당 학생의 친구들
        # print(new_seat[i][j])
        # print(last_freind)
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]

            if x < 0 or x >= N or y < 0 or y >= N:
                continue

            if new_seat[y][x] in last_friends:  # 친구가 앉아 있으면
                result_bf += 1

        # 점수 계산
        if result_bf == 1:
            result += 1
        elif result_bf == 2:
            result += 10
        elif result_bf == 3:
            result += 100
        elif result_bf == 4:
            result += 1000

# 최종 점수 출력
print(result)

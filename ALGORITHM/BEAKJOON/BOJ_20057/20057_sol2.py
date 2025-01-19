# 날리기
def flow(ny, nx):
    global result

    sand = maze[ny][nx]
    sy, sx = ny - 2, nx - 2
    last_y, last_x = -1, -1
    total = 0  # 이동한 모래 양을 합산할 변수

    for i in range(5):
        for j in range(5):
            if percentage[i][j] == -100:
                last_y = sy + i
                last_x = sx + j
                continue

            moved_sand = int(sand * percentage[i][j] * 0.01)  # 정수 변환
            total += moved_sand

            # 범위를 벗어난 경우
            if sy + i < 0 or sy + i >= N or sx + j < 0 or sx + j >= N:
                result += moved_sand
            else:
                maze[sy + i][sx + j] += moved_sand

    # 마지막 위치에 남은 모래 처리
    remaining_sand = sand - total  # 남은 모래 계산
    if last_y < 0 or last_y >= N or last_x < 0 or last_x >= N:
        result += remaining_sand
    else:
        maze[last_y][last_x] += remaining_sand

    maze[ny][nx] = 0  # 원래 위치는 빈칸으로


# 퍼센트 회전
def rotation():

    new_percentage=[[0]*5 for _ in range(5)]


    for i in range (5):
        for j in range (5):
            new_percentage[i][j] = percentage[j][5 -1 -i]
            # print(maze)
            # print(i,j)
    return new_percentage

# 입력
N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
result = 0

# 퍼센트 배열
percentage = [[0, 0, 2, 0, 0],
              [0, 10, 7, 1, 0],
              [5, -100, 0, 0, 0],
              [0, 10, 7, 1, 0],
              [0, 0, 2, 0, 0]]

# 방향
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

# 초기화
start = N // 2
y, x = start, start
to_go = 1
now_go = 0
direction = 0
cnt = 0

while True:
    now_go += 1
    nd = direction % 4

    # 이동
    y += dy[nd]
    x += dx[nd]
    if y < 0 or x < 0:
        break

    if maze[y][x] != 0:
        flow(y, x)

    if to_go == now_go:
        direction += 1
        now_go = 0
        cnt += 1
        percentage = rotation()
        if cnt == 2:
            cnt = 0
            to_go += 1

print(result)

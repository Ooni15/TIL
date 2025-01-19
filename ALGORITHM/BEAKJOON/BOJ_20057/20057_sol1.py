# 날리기
def flow(ny, nx):
    global result

    sand = maze[ny][nx]
    sy, sx = ny - 2, nx - 2
    last_y, last_x = -1, -1
    total = 0
    for i in range(5):
        for j in range(5):

            if percentage[i][j] == -100:
                last_y = sy + i
                last_x = sx + j
                continue



            if sy + i < 0 or sy + i >= N or sx + j < 0 or sx + j >= N:
                # print(result)
                result += int(sand * percentage[i][j] * 0.01)
                total += int(sand * percentage[i][j] * 0.01)
                # print(result)

            else:
                maze[sy + i][sx + j] += int(sand * percentage[i][j] * 0.01)
                total += int(sand * percentage[i][j] * 0.01)

    # print(last_y, last_x)
    if last_y < 0 or last_y >= N or last_x < 0 or last_x >= N:
        result += sand - total
        # print(result)
    else:
        maze[last_y][last_x] += sand - total

    maze[ny][nx] = 0

    # print(maze)


# 퍼센트 회전
def rotation():
    new_percentage = [[0] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            new_percentage[i][j] = percentage[j][5 - 1 - i]
            # print(maze)
            # print(i,j)
    return new_percentage


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
# 돌아보자잇!
# 가운데 좌표 시작임
start = N // 2
y, x = start, start
# 시작 좌표 maze[start][start]
to_go = 1  # 가야하는 칸 수 (for 달팽스)
now_go = 0  # 지금 내가 간 칸수 to_go 칸까지 하나씩 올려줘
direction = 0  # 방향 바꿀 변수
cnt = 0

while True:

    now_go += 1
    nd = direction % 4

    # 이동할게
    y += dy[nd]
    x += dx[nd]
    # print(percentage)
    if y < 0 or x < 0:
        break

    if maze[y][x] != 0:
        flow(y, x)

    if to_go == now_go:
        direction += 1
        # print(direction)
        now_go = 0
        cnt += 1
        percentage = rotation()

        if cnt == 2:
            cnt = 0
            to_go += 1

print(result)

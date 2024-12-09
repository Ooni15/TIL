from itertools import product

def make_comb(arr):
    global cctv_cnt
    comb = [0] * cctv_cnt
    for i in range(cctv_cnt):
        if arr[i] == 1 or arr[i] == 3 or arr[i] == 4:
            comb[i] = [1, 2, 3, 4]
        elif arr[i] == 2:
            comb[i] = [1, 2]
        elif arr[i] == 5:
            comb[i] = [1]
    combinations = list(product(*comb))
    return combinations

def camera_range(number, location, combi):
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(len(number)):
        y, x = location[i]
        if number[i] == 1:
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            dx, dy = directions[combi[i] - 1]
            check_direction(x, y, dx, dy, visited)
        elif number[i] == 2:
            if combi[i] == 1:
                check_direction(x, y, 1, 0, visited)
                check_direction(x, y, -1, 0, visited)
            else:
                check_direction(x, y, 0, 1, visited)
                check_direction(x, y, 0, -1, visited)
        elif number[i] == 3:
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            dx1, dy1 = directions[combi[i] - 1]
            dx2, dy2 = directions[combi[i] % 4]
            check_direction(x, y, dx1, dy1, visited)
            check_direction(x, y, dx2, dy2, visited)
        elif number[i] == 4:
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for j in range(4):
                if j != combi[i] - 1:
                    dx, dy = directions[j]
                    check_direction(x, y, dx, dy, visited)
        elif number[i] == 5:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                check_direction(x, y, dx, dy, visited)

    return sum(sum(row) for row in visited)

def check_direction(x, y, dx, dy, visited):
    while True:
        x += dx
        y += dy
        if x < 0 or x >= M or y < 0 or y >= N or room[y][x] == 6:
            break
        if room[y][x] == 0 and not visited[y][x]:
            visited[y][x] = 1

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
cctv_number = []
cctv_location = []
cctv_cnt = 0
wall_cnt = 0

for i in range(N):
    for j in range(M):
        if room[i][j] == 6:
            wall_cnt += 1
        elif room[i][j] != 0:
            cctv_number.append(room[i][j])
            cctv_location.append((i, j))
            cctv_cnt += 1

detect = make_comb(cctv_number)
result = [camera_range(cctv_number, cctv_location, d) for d in detect]

max_covered = max(result) if result else 0
final = (N * M) - cctv_cnt - wall_cnt - max_covered
print(final)
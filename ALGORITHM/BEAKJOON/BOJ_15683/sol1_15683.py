from itertools import product

# 조합 구하는 함수
def make_comb(arr):

    global cctv_cnt
    comb = [0] * cctv_cnt
    for i in range (cctv_cnt):
        if arr[i] == 1 or arr[i] == 3 or arr[i] == 4:
            comb[i] = [1,2,3,4]
        if arr[i] == 2:
            comb[i] = [1,2]
        if arr[i] == 5:
            comb[i] = [1]

    combinations = list(product(*comb))
    return combinations

# 탐색 담는 함수
def camera_range(number,location,combi):
    # CC 넘버, CC 위치, 현 CC 방향
    cnt = 0
    visited = [[0] * M for _ in range(N)]

    for i in  range(len(number)):
        y, x = location[i][0], location[i][1]
        dx, dy = 0, 0
        if number[i] == 1:

            if combi[i] == 1:
                dx = -1
            elif combi[i] == 2:
                dy = -1
            elif combi[i] == 3:
                dx = 1
            elif combi[i] == 4:
                dy = 1

            while True:
                x += dx
                y += dy

                if x < 0 or x >= M or y < 0 or y>=N or room[y][x] != 0:
                    break

                if not visited[y][x]:
                    visited[y][x] = 1

        elif number[i] == 2:
            if combi[i] == 1:
                dx = 1
                while True:
                    x += dx

                    if x < 0 or room[y][x] != 0:
                        break

                    if x >= M or room[y][x] != 0:
                        x = location[i][1]
                        dx = -1

                    if not visited[y][x]:
                        visited[y][x] = 1

            elif combi[i] == 2:
                dy = 1
                while True:
                    y += dy

                    if y < 0 or room[y][x] != 0:
                        break

                    if y >= N or room[y][x] != 0:
                        y = location[i][0]
                        dy = -1

                    if not visited[y][x]:
                        visited[y][x] = 1


        elif number[i] == 3:
            if combi[i] == 1:
                dy = -1
                while True:
                    y += dy
                    x += dx
                    if x >= M or room[y][x] != 0:
                        break

                    if y < 0 or room[y][x] != 0:
                        y = location[i][0]
                        x = location[i][1]
                        dy = 0
                        dx = 1

                    if not visited[y][x]:
                        visited[y][x] = 1
            elif combi[i] == 2:
                dy = 1
                while True:
                    y += dy
                    x += dx
                    if x >= M or room[y][x] != 0:
                        break

                    if y >= N or room[y][x] != 0:
                        y = location[i][0]
                        x = location[i][1]
                        dy = 0
                        dx = 1

                    if not visited[y][x]:
                        visited[y][x] = 1
            elif combi[i] == 3:
                dy = 1
                while True:
                    y += dy
                    x += dx
                    if x < 0 or room[y][x] != 0:
                        break

                    if y >= N or room[y][x] != 0:
                        y = location[i][0]
                        x = location[i][1]
                        dy = 0
                        dx = -1

                    if not visited[y][x]:
                        visited[y][x] = 1
            elif combi[i] == 4:
                dy = -1
                while True:
                    y += dy
                    x += dx
                    if x < 0 or room[y][x] != 0:
                        break

                    if y < 0 or room[y][x] != 0:
                        y = location[i][0]
                        x = location[i][1]
                        dy = 0
                        dx = -1

                    if not visited[y][x]:
                        visited[y][x] = 1

        elif number[i] == 4:
            if combi[i] == 1:
                dy = -1
                while True:
                    y += dy
                    x += dx
                    if x >= M or room[y][x] != 0:
                        break

                    if y < 0 or room[y][x] != 0:
                        y = location[i][0]
                        x = location[i][1]
                        dy = 0
                        dx = -1

                    if x < 0 or room[y][x] != 0:
                        y = location[i][0]
                        x = location[i][1]
                        dy = 0
                        dx = 1

                    if not visited[y][x]:
                        visited[y][x] = 1

            elif combi[i] == 2:
                dy = -1
                while True:
                    y += dy
                    x += dx
                    if y >= N or room[y][x] != 0:
                        break

                    if y < 0 or room[y][x] != 0:
                        y = location[i][0]
                        x = location[i][1]
                        dy = 0
                        dx = 1

                    if x >= M or room[y][x] != 0:
                        y = location[i][0]
                        x = location[i][1]
                        dy = 1
                        dx = 0

                    if not visited[y][x]:
                        visited[y][x] = 1

            elif combi[i] == 3:
                dy = 1
                while True:
                    y += dy
                    x += dx
                    if x < 0 or room[y][x] != 0:
                        break

                    if y >= N or room[y][x] != 0:
                        y = location[i][0]
                        x = location[i][1]
                        dy = 0
                        dx = 1

                    if x >= M or room[y][x] != 0:
                        y = location[i][0]
                        x = location[i][1]
                        dy = 0
                        dx = -1

                    if not visited[y][x]:
                        visited[y][x] = 1

            elif combi[i] == 4:
                dy = -1
                while True:
                    y += dy
                    x += dx
                    if y >= N or room[y][x] != 0:
                        break

                    if y < 0 or room[y][x] != 0:
                        y = location[i][0]
                        x = location[i][1]
                        dy = 0
                        dx = -1

                    if x < 0 or room[y][x] != 0:
                        y = location[i][0]
                        x = location[i][1]
                        dy = 1
                        dx = 0

                    if not visited[y][x]:
                        visited[y][x] = 1

        if number[i] == 5:
            dy = -1

            while True:
                y += dy
                print(y)
                x += dx

                if x >= M or room[y][x] != 0:
                    break

                if y >= N or room[y][x] != 0:
                    y = location[i][0]
                    x = location[i][1]
                    dy = 0
                    dx = 1

                elif y < 0 or room[y][x] != 0 :
                    y = location[i][0]
                    x = location[i][1]
                    dy = 0
                    dx = -1

                elif x < 0 or room[y][x] != 0:
                    y = location[i][0]
                    x = location[i][1]
                    dy = 1
                    dx = 0

                if not visited[y][x]:
                    visited[y][x] = 1

    re_sum = 0
    for i in range(N):
        re_sum += sum(visited[i])

    if re_sum == 15:
        print(visited)
    return re_sum


# main
N, M = map(int,input().split())
room = [list(map(int,input().split())) for _ in range (N)]
cctv_number = []
cctv_location = []
cctv_cnt = 0
wall_cnt = 0

#  CCTV 개수, 번호, 위치 저장
for i in range (N):
    for j in range(M):
        if room[i][j] == 0:
            continue

        if room[i][j] == 1:
            cctv_number.append(1)
        elif room[i][j] == 2:
            cctv_number.append(2)
        elif room[i][j] == 3:
            cctv_number.append(3)
        elif room[i][j] == 4:
            cctv_number.append(4)
        elif room[i][j] == 5:
            cctv_number.append(5)
        elif room[i][j] == 6:
            wall_cnt += 1
            continue

        cctv_cnt += 1
        cctv_location.append([i, j])

# print(make_comb(cctv_number))
# 조함 구하기 성공!
detect = make_comb((cctv_number))

# 조합별로 bfs 돌려볼게요!
# 여기서 해야할 일!
# 매치 시킬 아이들 씨씨넘버, 씨씨위치, 디텍트배열 내의 아이들
result = [0] * len(detect)


for i in range(len(detect)):
    result[i] = camera_range(cctv_number,cctv_location,detect[i])
print(result)
print(max(result))
# 수정되면 CCTV 빼지마
print(cctv_cnt, wall_cnt, max(result))
final = (N * M) - cctv_cnt - wall_cnt - max(result)
# CC
print(f'정답',final)
from collections import deque
# import sys
# sys.stdin = open('input.txt', 'r')

def way(type):
    number = 2

    if type == 1:
        number = 4
        dx = [0, 0, 0, -1, 1]  # 상하좌우
        dy = [0, -1, 1, 0, 0]

    if type == 2:
        dx = [0, 0, 0]  # 상하
        dy = [0, -1, 1]

    if type == 3:
        dx = [0, -1, 1]  # 좌 우
        dy = [0, 0, 0]

    if type == 4:
        dx = [0, 0, 1]  # 상 우
        dy = [0, -1, 0]

    if type == 5:
        dx = [0, 0, 1]  # 하 우
        dy = [0, 1, 0]

    if type == 6:
        dx = [0, 0, 1]  # 하 좌
        dy = [0, 1, 0]

    if type == 7:
        dx = [0, 0, -1]  # 상 좌
        dy = [0, -1, 0]

    return number, dx, dy

def bfs(row, col, level, px, py):
    cnt = 1
    type = tunnel[row][col]
    queue = deque([(row, col, cnt, type, 0, 0)])
    visited[row][col] = True

    while queue:
        info = queue.popleft()
        r, c, cnt, type, px, py = info[0], info[1], info[2], info[3], info[4], info[5]

        if cnt == level:
            continue  # Level에 도달했을 때 탐색을 중지하지만, 다른 경로는 계속 처리

        num, dy, dx = way(type)


        for k in range(num + 1):
            nr = r + dx[k]
            nc = c + dy[k]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if tunnel[nr][nc] == 0:
                continue

            find = False

            for k in range(num):
                if dx[k] +
                nc = c + dy[k]

                if not visited[nr][nc]:
                    queue.append((nr, nc, cnt + 1, tunnel[nr][nc], dx[k], dy[k]))
                    visited[nr][nc] = True


T = int(input())

for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())  # N : 세로, M : 가로, R : 세로위치, C : 가로위치, L : 탈출 후 위치
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    type = tunnel[R][C]  # 터널 타입
    visited = [[False] * M for _ in range(N)]
    bfs(R, C, L, 0, 0)

    for row in visited:
        total += sum(row)

    print(f'#{test_case} {total}')

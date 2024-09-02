from collections import deque
def bfs_cost(start_x, start_y) :

    cost = 0

    queue = deque([[start_x, start_y, cost]])
    visited[start_x][start_y] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue :

        info = queue.popleft()
        X = info[0]
        Y = info[1]
        cost = info[2]

        # 상하좌우 탐색
        for k in range (4) :
            ni = X + dx[k]
            nj = Y + dy[k]

            if 0 <= ni < M and 0 <= nj < N :
                if arr[ni][nj] == 'L' :
                    queue.append([ni, nj, cost + 1])
                    visited[ni][nj] = True
                else :      # 'W'이면
                    return cost
                    break

# main
T = int(input())

for test_case in range (1, T + 1) :
    N, M = map(int,input().split())
    arr = [list(map(str,input())) for _ in range (N)]

    cost = 0

    for i in range (N) :
        for j in range(M) :
            if arr[i][j] == 'L' :
                visited = [[False] * (M + 1) for _ in range(M)]
                cost += bfs_cost(i, j)

    print(f'#{test_case}', cost)
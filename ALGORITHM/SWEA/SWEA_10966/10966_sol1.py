from collections import deque
def bfs_cost() :
    global arr, visited

    queue = deque()

    for i in range (N) :
        for j in range (M) :
            if arr[i][j] == 'W' :
                visited[i][j] = 0
                queue.append((i , j))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue :

        X, Y = queue.popleft()

        # 상하좌우 탐색
        for k in range (4) :
            ni = X + dx[k]
            nj = Y + dy[k]

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                visited[ni][nj] = visited[X][Y] + 1
                queue.append((ni, nj))

            # if 0 > ni or ni >= N or 0 > nj or nj >= M :
            #     continue
            #
            # if visited[ni][nj] != -1 :
            #     continue
            #
            #
            # visited[ni][nj] = visited[X][Y] + 1
            # queue.append((ni, nj))

# main
T = int(input())

for test_case in range (1, T + 1) :
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range (N)]

    cost = 0

    visited = [[-1] * M for _ in range (N)]
    bfs_cost()

    #print(visited)
    for i in range(N) :
        for j in range(M) :
            cost += visited[i][j]

    print(f'#{test_case}', cost)

"""
2 3
WLL
LLL
"""
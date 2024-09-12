from collections import deque

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]

def bfs(x, y, case) :

    cnt = 1
    queue = deque([(x, y, case)])
    visited[x][y] = True

    while queue :
        info = queue.popleft()
        x, y, case = info[0], info[1], info[2]

        for k in range (4) :
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx > M - 1 or ny < 0 or ny > N - 1 :
                continue

            if visited[nx][ny]  :
                continue

            if case == 1 and arr[nx][ny] == 'W' :
                queue.append((nx, ny, 1))
                visited[nx][ny] = True
                cnt += 1
                continue

            if case == 2 and arr[nx][ny] == 'B' :
                queue.append((nx, ny, 2))
                cnt += 1
                visited[nx][ny] = True

    return cnt**2


# main
N, M = map(int,input().split())
arr = [list(input()) for _ in range(M)]

visited = [[0] * (N) for _ in range(M)]
w_power, b_power = 0, 0

for i in range(M) :
    for j in range (N) :
        if not visited[i][j] :
            if arr[i][j] == 'W' :
                w_power += bfs(i, j, 1)
            else :
                b_power += bfs(i, j , 2)

print(w_power, b_power)
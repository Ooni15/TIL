from collections import deque


dy = [0, 0, -1, 1]  # 상 하 좌 우
dx = [-1, 1, 0, 0]

def bfs(x, y) :

    cnt = 1
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue :

        info = queue.popleft()
        x, y = info[0], info[1]

        for i in range(4):
            ny = x + dx[i]
            nx = y + dy[i]

            if ny < 1 or ny > N or nx < 1 or nx > M:
                continue

            if visited[ny][nx] or arr[ny][nx] == 0:
                continue

            queue.append((ny, nx))
            visited[ny][nx] = True
            cnt += 1

    return cnt





N, M, K = map(int, input().split())

arr = [[0] * (M + 1) for _ in range (N + 1)]
to_go = [0] * K
visited = [[False] * (M + 1) for _ in range (N + 1)]
max_value = 0
cnt = 0

for i in range (K) :

    a, b = map(int,input().split())
    arr[a][b] = 1
    to_go[i] = [a, b]

for i in range (K) :
    a = to_go[i][0]
    b = to_go[i][1]
    if not visited[a][b] :
        value = bfs(a,b)
        if max_value < value :
            max_value = value


print(max_value)
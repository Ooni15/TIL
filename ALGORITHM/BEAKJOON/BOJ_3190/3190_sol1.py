from collections import deque

# N X N 의 배열
N = int(input())
arr = [[0]*N for _ in range(N)]

# K개의 사과
K = int(input())
for i in range(K):
    a, b = map(int,input().split())
    arr[a-1][b-1] = 100     # 사과사과

print(arr)
cnt = 0

# queue에 넣기

dy = [0, 1, 0, -1]      # 동 남 서 북
dx = [1, 0, -1, 0]
n_dir = 0       # 현 방향
ny, nx = 0, 0
# 큐에 넣어
snake = deque([(ny,nx)])
arr[0][0] = 10
# snake = deque()
# X초 탐색
X = int(input())
# 터트릴 조건
result = 0

for i in range(X):
    final, dir = map(str,input().split())
    final = int(final)

    if i == X-1 :
        final += N

    while cnt <= final:
        ny += dy[n_dir]
        nx += dx[n_dir]

        print(f"ny: {ny}, nx: {nx}, direction: {n_dir}, cnt: {cnt}")

        # 벽에 닿으면 터져
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            result = 1
            break
        # 내 몸이면 터져
        if arr[ny][nx] == 10 :
            result = 1
            break

        # 사과면
        if arr[ny][nx] == 100 :
            snake.append((ny,nx))
            arr[ny][nx] = 10

        if arr[ny][nx] == 0:
            oy,ox = snake.popleft()
            arr[oy][ox] = 0
            snake.append((ny,nx))
            arr[ny][nx] = 10

        cnt += 1

    if result == 1:
        break

    if dir == 'L':
        n_dir = (n_dir - 1 + 4) % 4
    else :
        n_dir = (n_dir + 1) % 4





print(cnt)
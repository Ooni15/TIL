from collections import deque

dy = [-1, 1, 0, 0]  # 상하좌우
dx = [0, 0, -1, 1]
# bfs
def bfs(y, x, K) :

    queue = deque([(y,x)])

    while queue:
        yy, xx = queue.popleft()
        for i in range(4):
            ny = yy + dy[i]
            nx = xx + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= N :
                continue

            if arr[ny][nx] <= K or visited[ny][nx]:
                continue

            queue.append((ny,nx))
            visited[ny][nx] = True


# main
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
# visited = [[False] * N for _ in range(N)]
max_point = [0] * N

for i in range(N):
    max_point[i] = max(arr[i])

M = max(max_point)

cnt_box = [0] * (M+1)
for k in range(0, M + 1):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and not visited[i][j] :
                # print(arr[i][j])
                bfs(i, j, k)
                cnt += 1
    cnt_box[k] = cnt

# print(cnt_box)
print(max(cnt_box))
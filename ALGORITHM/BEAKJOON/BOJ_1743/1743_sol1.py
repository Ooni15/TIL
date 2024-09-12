## 시간초과

dy = [0, 0, -1, 1]  # 상 하 좌 우
dx = [-1, 1, 0, 0]

def dfs(x, y) :

    global cnt

    visited[x][y] = True
    cnt += 1


    for i in range(4) :
        ny =  x + dx[i]
        nx =  y + dy[i]

        if ny < 1 or ny > N or nx < 1 or nx > M :
            continue

        if visited[ny][nx] or arr[ny][nx] == 0 :
            continue

        dfs(ny,nx)



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
        cnt = 0
        dfs(a,b)
        if max_value < cnt :
            max_value = cnt


print(max_value)




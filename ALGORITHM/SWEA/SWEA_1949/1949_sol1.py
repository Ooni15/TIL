dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 최대 지점 찾기
def max_point(lst) :
    place = []
    max_high = 0
    for i in range(N):
        high = max(lst[i])
        if max_high <= high :
            max_high = high

    for i in range(N):
        for j in range(N):
            if lst[i][j] == max_high :
                place.append([i,j])

    return place

# dfs 만들어야징
def dfs(X, Y, L) :
    global max_len, cnt, h

    max_len = max(max_len, L)

    for i in range(4) :
        nx = X + dx[i]
        ny = Y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N :
            continue

        if visited[nx][ny] :
            continue

        # cnt 세기
        # K가 0이고 옆에 애가 작으면 끝!
        if K == 0 and arr[nx][ny] >= arr[X][Y] :
            continue

        # 작으면 모가지 쳐버려
        elif arr[nx][ny] >= arr[X][Y] and cnt == 0 :
            # 아니 이거 이상하다잇
            for i in range (1, K + 1) :
                if arr[nx][ny] - i < arr[X][Y] :
                    h = i
                    cnt += 1
                    break

            if h == 0 :
                continue

            original_height = arr[nx][ny]
            arr[nx][ny]-= h
            visited[nx][ny] = True
            dfs(nx, ny, L + 1)
            visited[nx][ny] = False
            arr[nx][ny] = original_height
            cnt = 0
            h= 0

        # 내가 더 크면 가버령!
        elif arr[nx][ny] < arr[X][Y] :
            visited[nx][ny] = True
            dfs(nx, ny, L + 1)
            visited[nx][ny] = False

# main
T = int(input())

for test_case in range(1, T + 1) :
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_len = 0
    # 최대 높이인 애 찾기
    places = max_point(arr)  # 위치 배열 겟챠~!~!

    # bfs
    for place in places:
        a, b = place[0], place[1]
        visited = [[False] * N for _ in range(N)]
        l = 1
        cnt = 0
        h = 0
        visited[a][b] = True
        dfs(a,b, l)

    print(f'#{test_case}', max_len)







'''
1
5 1
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
'''
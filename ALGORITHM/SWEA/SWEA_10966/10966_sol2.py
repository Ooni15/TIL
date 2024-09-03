from collections import deque

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
T = int(input())
for tc in range(1, T + 1):
    # 지도 행과 열의 크기
    N, M = map(int, input().split())
    # 지도 ( W: 물, L: 땅)
    grid = [input().strip() for _ in range(N)]
    result = 0  # 모든 최소 이동거리를 합한 결과를 저장할 변수
    visited = [[-9999] * M for _ in range(N)]  # 문제에서 N <= 1000

    queue = deque()
    # 모든 물('W')를 큐에 추가
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'W':
                queue.append((i,j))
                # 주변 땅을 1로 바꿔야 하니까
                # BFS라는게 본인 기준으로 1칸 , 본인이 0이여야죠
                visited[i][j] = 0

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:  # 리스트 순회 ( 4방향 순회)
            nx, ny = cx + dx, cy + dy  # 다음 이동할 좌표

            # if 0 <= nx < N and 0 <= ny < M and visited[] and `~~~~~~~:
                # 로직 작성
            # 이동할 좌표가 범위 벗어나면
            if 0 > nx or nx >= N or 0 > ny or ny >= M: continue

            # 갱신된 적이 있으면, 그냥 넘어간다~~~
            if visited[nx][ny] != -9999: continue

            # 갱신된적도 없고, 이동도 가능하고 ~~
            visited[nx][ny] = visited[cx][cy] + 1
            queue.append((nx, ny))

    #print(visited)
    for i in range(N):
        for j in range(M):
            # 이동거리는 => visited
            result += visited[i][j]

    print(f"#{tc} {result}")

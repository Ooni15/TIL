from collections import deque
# main
T = int(input())

for test_case in range (1, T + 1) :
    N, M = map(int,input().split())
    arr = [list(map(str,input())) for _ in range (N)]
    grid = [input().strip() for _ in range(N)]
    result = 0        #
    visited = [[-1] * M for _ in range (N)]     # 문제에서 N <= 1000

    # 물은 0으로 만들고 나머지는 그대로 둘거임
    queue = deque()

    for i in range (N) :
        for j in range(M) :
            if arr[i][j] == 'W' :
                queue.append((i,j))
                visited[i][j] = 0   # 주변 땅을 1로 바꿔야하니까

    while queue :
        cx, cy = queue.popleft()
        dxy = [()]
    print(f'#{test_case}', cost)
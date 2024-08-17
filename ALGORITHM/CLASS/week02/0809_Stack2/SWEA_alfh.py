import sys
sys.stdin = open('sample_input (6).txt')

"""
델타 탐색의 다른 방법
for dx, dy in [(-1, 0),(1, 0),(0, -1),(0, 1)] :
"""
# 상하좌우 델타 값
dx = [-1, 1, 0, 0]  # direction x
dy = [0, 0, -1, 1]  # direction y

def search (x,y) :
    stack = [(x,y)]
    visited[x][y] = 1
    # 언제까지 탐색을 할 것인가
    while stack :   # 스택이 없을 때까지 / 방문할 곳이 있으면 계속 돈다잇~
        x, y = stack.pop()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로의 범위를 벗어나지 않는지 &&
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and visited[nx][ny] != 1:
                if maze[nx][ny] == 3 :  # 다음 위치가 출구임
                    return 1    # 1 반환 후 함수 종료
                # 3이 아니라면,
                stack.append((nx,ny))
                visited[nx][ny] = 1
    return 0

T = int(input())

for tc in range(1, T + 1) :
    N = int(input())

    maze = [list(map(int,input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 2가 담긴곳 == 출발점
    for i in range(N) :
        for j in range(N) :
            if maze[i][j] == 2:
                print(f'#{tc} {search(i, j)}')

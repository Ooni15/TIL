from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

def way(type) :
    number = 2

    if type == 1 :
        number = 4
        dx = [0,0, 0, -1, 1]  # 상하좌우
        dy = [0,-1, 1, 0, 0]

    if type == 2 :
        dx = [0, 0, 0]     # 상하
        dy = [0,-1, 1]

    if type == 3:
        dx = [0, -1, 1]   # 좌 우
        dy = [0, 0, 0]

    if type == 4 :
        dx = [0, 0, 1]  # 상 우
        dy = [0, -1, 0]

    if type == 5 :
        dx = [0, 0, 1]  # 하 우
        dy = [0, 1, 0]

    if type == 6 :
        dx = [0, 0, 1]  # 하 좌
        dy = [0, 1, 0]

    if type == 7 :
        dx = [0, 0, -1]  # 상 좌
        dy = [0, -1, 0]

    return number, dx, dy

def bfs (row, col, level, px, py) :     # 현위치, level

    cnt = 1
    type = tunnel[row][col]
    queue = deque([(row, col, cnt, type, 0, 0)])
    visited[row][col] = True

    while queue :

        info = queue.popleft()
        r, c, cnt, type, px, py = info[0], info[1], info[2], info[3], info[4], info[5]

        if cnt == level :
            continue      # 이걸 어케해야하지 continue 인가


        num, dy, dx = way(type)
        find = 0



        if find > 0  :

            for k in range(1, num + 1) :
                nr = r + dx[k]
                nc = c + dy[k]
                if nr < 0 or nr >= N or nc < 0 or nc >= M :
                    continue

                if visited[nr][nc] or tunnel[nr][nc] == 0 :
                    continue

                for i in range(num + 1):
                    if -px == dx[k] and -py == dy[k]:
                        find += 1
                if not visited[nr][nc] :
                    queue.append((nr, nc, cnt + 1, tunnel[nr][nc], dx[k], dy[k]))
                    visited[nr][nc] = True


T = int(input())

for test_case in range (1, T + 1) :
    N, M, R, C, L = map(int,input().split())    # N : 세로, M : 가로, R : 세로위치, C : 가로위치, L : 탈출 후 위치
    tunnel = [list(map(int,input().split())) for _ in range (N)]
    total = 0
    type = tunnel[R][C]     # 터널 타입
    visited = [[False] * M for _ in range (N)]
    queue = deque([(R, C, 1, type)])
    visited[R][C] = True
    bfs(R, C, L, 0, 0)

    for row in visited :
        total += sum(row)

    print(visited)
    print(f'#{test_case} {total}')

'''
1
5 6 2 1 3
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
'''
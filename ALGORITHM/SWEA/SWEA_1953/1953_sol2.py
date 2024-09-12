from collections import deque
# import sys
# sys.stdin = open('input.txt', 'r')
dy = [[], []]
dx = [[]]
T = int(input())

for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())  # N : 세로, M : 가로, R : 세로위치, C : 가로위치, L : 탈출 후 위치
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    type = tunnel[R][C]  # 터널 타입
    visited = [[False] * M for _ in range(N)]
    bfs(R, C, L, 0, 0)

    for row in visited:
        total += sum(row)

    print(f'#{test_case} {total}')

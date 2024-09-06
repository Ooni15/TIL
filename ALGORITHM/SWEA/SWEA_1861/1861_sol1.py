import sys
sys.stdin = open('input.txt', 'r')

# 접근 방법 2
# 1. 전체 배열을 순회하면서 확인한다.
# 2. 인접한 숫자가 현재 방보다 1 크면 visited 1 체크
#  - 1이 크면 다음으로 갈 수 있다.
# -> 정리 : 다음으로 갈 수 있는 방이다 라는 정보를 저장

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for test_case in range(1, T + 1) :

    N = int(input())
    arr = [list(map(int,input().split())) for _ in range (N)]

    # index 에러 조심!
    visited = [0] * (N * N + 1)

    # 전체를 순회하며
    # 상하좌우에 나보다 1이 크면, visited에 체크
    for i in range (N) :
        for j in range (N) :
            for k in range (4) :
                # ny, nx는 다음 좌표
                ny = i + dy[k]
                nx = j + dx[k]

                if ny < 0 or ny >= N or nx < 0 or nx >= N :
                    continue

                # 내 옆이 나보다 1 크다면, 나는 다음으로 갈 수 있는 방이다.
                if arr[ny][nx] == arr[i][j] + 1 :
                    visited[arr[i][j]] = 1
                    # 이미 체크된 순간, 다른 방향은 볼 필요가 없음
                    # 이유 : 동일한 숫자가 없기 때문
                    break

    # cnt : 하나씩 체크 / max_cnt : 정답(최대값) / start : 계산을 시작할 위치
    cnt = max_cnt = start = 0


    for i in range (N * N - 1, -1, -1) :
        if visited[i]:
            cnt += 1
        else :
            if max_cnt <= cnt :
                max_cnt = cnt
                start = i + 1
            cnt = 0       # cnt 초기화

    print(f'#{test_case} {start} {max_cnt + 1}')





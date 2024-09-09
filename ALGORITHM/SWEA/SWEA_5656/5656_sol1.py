# 뭔가 잘못됐다.... 안돌아간디 코드 확인해라

# 모든 위치에서 시도해본다.  N번 반복한다.
# 추가로 제거될 벽들의 위치와 적힌 숫자를 저장해둔다.
# 특정 시점으로부터 구슬을 쏴야함

import sys
sys.stdin = open('input.txt', 'r')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def shoot(level, remains, now_arr) :
    global min_blocks

    # 기저 조건
    # 구슬을 모두 발사 or 남은 벽돌이 0 이면 종료
    if level == N or remains == 0 :
        # 최소값 갱신
        min_blocks = min(min_blocks, remains)
        return

    # 1. 한 줄씩 쏘자
    #   -> 벽돌이 깨진 상태
    #   -> 중력
    for col in range (W) :
        # 방법 1.
        # 1. col 위치에 쏘기 전 상태를 복사
        # 2. 원본 리스트의 col 위치에 구슬을 쏜다.
        # 3. level + 1번 상태로 이동 (다음 재귀 호출)
        # 4. col 위치에 쏘기 전 상태로 복구

        # 방법 2.
        # 1. col 위치에 쏘기 전 상태를 복사
        # 2. 복사한 리스트의 col 위치에 구슬을 쏜다.
        # 3.  level + 1번 상태로 이동 (다음 재귀 호출) + col 위치에 쏘고 난 상태를 함께께 전달

        copy_arr = [row[:] for row in now_arr]

        # col 위치에 구슬을 쏘자!
        # 1. 구슬을 쏘는 열에서 가장 위에 있는 벽돌 찾기
        row = -1 # 벽돌잉 ㅓㅄ다고 가정
        for r in range (H) :
            if copy_arr[r][col] : # r 위치에 벽돌이 있다면
                row = r
                break

        if row == -1 : # 벽돌이 없는 열이면 다음 열로 넘어가자
            continue

        # 2. 연쇄적으로 벽돌이 깨짐
        li = [(row, col, copy_arr[row][col])]    # 앞으로 깨져야할 벽돌을 저장
        now_remains = remains - 1   # 현재 남은 벽돌 -1
        copy_arr[row][col] = 0  # 구스리 처음 만나는 벽돌 깨짐 처리

        while li :
            r, c, p = li.pop()  # 앞에서 빼든 뒤에서 빼든 상관 X
            for k in range (1, p) : # power만큼 퍼지면서 꺠진다.
                for i in range (4) :    # 상하좌우
                    nr = r + (dy[i] * k)
                    nc = c + (dx[i] * k)

                    if nr < 0 or nr >= H or nc < 0 or nc >= W : # 범위 계산
                        continue

                    if copy_arr[nr][nc] == 0 :
                        continue

                    li.append((nr,nc,copy_arr[nr][nc]))     # 다음 벽돌 추가
                    copy_arr[nr][nc] = 0
                    now_remains -= 1

            # 빈칸 메꾸기
            for c in range(W) : # 전체 열들을 확인
                idx = H - 1     # 벽돌이 위치할 index
                for r in range(H-1, -1, -1) :
                    if copy_arr[r][c] :     # 벽돌이 있으면 무조건 SWAP 하도록
                        # idx와 r이 같아도 바꾼다 == 의미없는 교환
                        # 가독성을 위해서 아래와 같이 구현
                        copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                        idx -= 1

            shoot(level + 1, now_remains, copy_arr)


T = int(input())

for test_case in range (1, T + 1) :
    N, W, H = map(int, input().split())

    # 1. 최소 벽돌
    #   - 몇 개 남았을까? 계산해야한다. -> 2차원 리스트를 순회함녀서 매 번 계산하면 너무 느리다.
    #   - 현재 남은 벽돌 수를 통해 해결됨!
    # 2. 현재 벽돌이 다 깨지면(남은 벽돌이 없다) 더 이상 진행할 필요가 없다!
    #   - 현재 벽돌 수 같이 저장하면 좋을 것 같다.
    # 3. N 번 구슬을 쏘자.
    #   - 시작점 : 0번  / 하나도 안깨진 벽돌 수
    #   - 끝점 : N번 쏘면 끝 / 벽돌이 다 깨지면 끝

    arr = [list(map(int,input().split())) for _ in range (H)]
    min_blocks = 1e9
    blocks = 0

    # 현재 벽돌 수 계산
    for row in arr :
        for el in row :
            if el : # 0 보다 크면 벽돌임
                blocks += 1

    shoot(0, blocks, arr)    # 시작점, 남은 벽돌 수

    print(f'#{test_case} {min_blocks}')
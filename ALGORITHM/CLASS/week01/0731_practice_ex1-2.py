# 2차원 배열 델타
# 델타를 이용한 2차원 배열 탐색
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
#
# print(arr)
#
# di = [0, 1, 0,-1]
# dj = [1, 0, -1, 0]
#
"""
5
45 15 10 56 23
96 98 99 40 60
96 84 49 46 34
16 64 81 4 11
10 66 85 55 14
"""
# total = 0
# for i in range(N) :
#     for j in range(N) : # NxN 배열의 모든 원소에 대해
#         s = 0           # 절대 값의 합 저장
#         # i, j 원소의 4 방향 원소에 대해
#         for k in range(4) :
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni< N and 0 <=nj < N:
#                 s += abs(arr[i][j] - arr[ni][nj])  # 실존하는 인접원소 ni,nj
#         total += s
#
# print(total)


# 파이썬은 음수 인덱스를 사용해도 에러가 뜨지 않는다.
# 1. 넘어갔을 경우
# 2. 안넘어갔을 경우
# Falsy, Truthy 어떤 값이 True or False로 평가되는가
# 부정연산자
# is_safe : 가도 괜찮은지를 평가 후 Boolean을 반환
    # True : NXM  내에 있다.
    # not is_safe :
        # 로직 수행 X
    # is_safe :
        # 로직 수행

num_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, +1]
# 5의 입장에서 상, 하, 좌, 우에 있는 숫자 출력하기
for row in range(len(num_list)) :
    #print('r', r)
    for column in range(len(num_list[0])) :
        #print(num_list[row]) # [1, 2, 3]
        tmp = num_list[row]
        # if num_list[r][c] == 5 :
        if tmp[column] == 5:    # 값이 5라면
            # 상 하 좌 우
            print(num_list[row-1][column])  # 상
            print(num_list[row+1][column])  # 하
            print(num_list[row][column-1])  # 좌
            print(num_list[row][column+1])  # 우

# 벽을 넘어가는 경우 아무것도 수행하지 않음.
num_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, +1]
x = 1
y = 1 # 5를 기준으로 사방 탐색

for d in range(4) :
    # 다음 행 & 다음 열 정의 필요 -> 이동 후 새로운 위치 좌표
    nx = x + d_row[d]
    ny = y + d_col[d]

    # map/ 범위를 벗어나는지 체크
    if nx < 0 or nx >= len(num_list) or ny < 0 or ny > len(num_list) :
        # 종료하기 : break
        # 지나치기 : continue
        print(num_list[nx][ny]) #


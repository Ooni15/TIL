N = int(input())
arr = [list(map(int,input().split())) for _ in range (N**2)]

num = [0] * N**2
friends= [0] * N**2
result = 0
# 순서 배열
count_arr = [0] * (N**2 + 1)
for i in range(N**2):
    num[i] = arr[i][0]
    friends[i] = arr[i][1:]

new_seat = [[-100]*N for _ in range(N)]

dx = [0, 0, -1, 1]  # 상하좌우
dy = [-1, 1, 0, 0]
for i in range(N**2):

    my_num =  num[i]
    my_friends = friends[i]
    count_arr[my_num] = i
    bf_max = -1     # 항상 갱신이 될 수 있게 -1로 잡아야 해
    empty_max = -1
    now_y, now_x = -1, -1
    # 내 주변 옆자리 확인하기
    for k in range(N):
        for t in range(N):
            bf = 0
            empty = 0

            seat = new_seat[k][t]
            # 누가 앉아 있으면 넘어가

            if seat != -100:
                continue

            # 각 자리별 완탐
            for n in range(4):
                y = k + dy[n]
                x = t + dx[n]

                if x < 0 or x>= N or y < 0 or y>= N:
                    continue


                if new_seat[y][x] == -100:
                    empty += 1
                elif new_seat[y][x] in my_friends:
                    bf += 1


            if bf_max < bf:
                bf_max = bf
                # 이거 넣어줘야해!!
                empty_max = empty
                now_y = k
                now_x = t
            elif bf_max == bf:
                if empty_max < empty:
                    empty_max = empty
                    now_y = k
                    now_x = t
            # if bf > bf_max or (bf == bf_max and empty > empty_max) or (
            #         bf == bf_max and empty == empty_max and (now_y > k or (now_y == k and now_x > t))):
            #     bf_max = bf
            #     empty_max = empty
            #     now_y, now_x = k, t


    new_seat[now_y][now_x] = my_num

# print(new_seat)

for i in range(N):
    for j in range(N):
        result_bf = 0
        last_freind = friends[count_arr[new_seat[i][j]]]
        # print(new_seat[i][j])
        # print(last_freind)
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]

            if x < 0 or x >= N or y < 0 or y >= N:
                continue

            if new_seat[y][x] in last_freind:
                # print(new_seat[y][x])
                result_bf += 1

        # print(result_bf)
        if result_bf == 1:
            result += 1
        elif result_bf == 2:
            result += 10
        elif result_bf == 3:
            result += 100
        elif result_bf == 4:
            result += 1000

# print(new_seat)
print(result)

"""
3
5 6 1 8 4
6 7 4 8 2
7 3 1 6 9
4 1 6 9 7
8 5 4 6 3
2 6 4 3 7
1 2 5 8 4
9 4 7 5 6
3 4 1 6 5
"""


'''
3
1 2 3 4 5
2 3 4 5 6
3 1 4 5 6
4 5 6 7 8
5 1 3 4 6
6 4 5 7 8
7 1 2 8 9
8 3 4 7 9
9 5 6 7 8
'''
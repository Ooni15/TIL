from collections import deque
# 미로의 출발점과 끝 점 찾는 함수
def Start (Arr, N) :

    for i in range (N) :
        for j in range (N) :
            if Arr[i][j] == 2 :
                return i, j
                break

# bfs 함수
def bfs_cost (Arr ,Start_x, Start_y) :

    cost = 0
    queue = deque([[Start_x, Start_y, cost]])       # queue에 시작점 x좌표, y좌표, cost 넣어줌
    Arr[Start_x][Start_y] = -1                      # 방문 처리
    #print(queue)
    dx = [1 ,-1 , 0, 0]
    dy = [0, 0, 1, -1]

    while queue :

        info = queue.popleft()
        #print(info)
        X = info[0]
        Y = info[1]
        cost = info[2]

        # 상하좌우 탐색
        for k in range(4) :
            ni = X + dx[k]
            nj = Y + dy[k]
            if 0 <= ni < N  and 0 <= nj < N  :
                #print('Arr[1][1]',Arr[1][1])
                #print('Arr[2][1]', Arr[2][1])
                if Arr[ni][nj] == 0 :       # 통로이면

                    Arr[ni][nj] = -1       # 방문 표시 -1


                    #print([ni, nj, cost + 1])
                    queue.append([ni, nj, cost + 1])    # cost 값 1 더해서 좌표와 append
                elif Arr[ni][nj] == 3:      # 도착지이면
                    Arr[ni][nj] == -1       # 방문표시
                    return cost             # 최종 비용 return 후 break
                    break

        if len(queue) == 0 :        # 전체 탐색을 했는데도 없으면 0 return
            return 0
            break

    print(Arr)



T = int(input())

for test_case in range (1, T + 1) :
    N = int(input())
    maze = [list(map(int,input()))for _ in range (N)]
    #print(maze)
    x, y = Start(maze, N)   # 시작 지점 찾기
    #print(x,y)
    print(f'#{test_case}', bfs_cost(maze, x, y))    # 탐색

'''
1
5
13101
10101
10101
10101
10021
'''
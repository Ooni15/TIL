from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(X, Y) :

    global abc
    queue = deque(([(X,Y)]))
    arr[X][Y] = -1


    while queue :
        info = queue.popleft()
        x, y = info[0], info[1]

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx< 0 or nx >= N or ny < 0 or ny >= N :
                continue

            if arr[nx][ny] <= 0 :
                continue

            queue.append([nx,ny])
            arr[nx][ny] = -1
            abc += 1





# main
N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
cnt = 0         # 단지 수
lst = []        # 몇 개 있는 지 넣을 리스트
abc = 1         # 단지 수 카운트

for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 1 :
            bfs(i, j)
            lst.append(abc)
            cnt += 1
            abc = 1


answer = sorted(lst)

print(cnt)
for i in range(len(answer)) :
    print(answer[i])
from collections import deque

N, M = map(int,input().split())
arr = [[0]* (M +1)]
for _ in range (N) :
    line = input()
    arr.append([0] + [int(char) for char in line])

queue = deque([[1, 1, 1]])
#print(queue)
arr[1][1] = 0

# 탐색 구간
dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]

while queue :
    info = queue.popleft()
    #print(info)
    x = info[0]
    y = info[1]
    cnt = info[2]

    if x == N and y == M :
        print(cnt)
        break

    for i in range (4) :
        ni = x + dx[i]
        nj = y + dy[i]
        if 1 <= ni < N + 1 and 1 <= nj < M + 1 :
            if arr[ni][nj] == 1 :
                arr[ni][nj] = 0     # 상태변경
                queue.append([ni, nj, cnt +1])



'''
4 6 
101111
101010
101011
111011
'''
# dfs
def dfs(start) :

    visited[start] = True
    # print(start, end= ' ')

    for i in graph[start] :
        if not visited[i] :
            dfs(i)

# main
T = int(input())

for test_case in range( 1, T + 1 ):
    N, M = map(int, input().split())

    # 그래프 만들기
    graph = [[] for _ in range(N + 1)]

    for i in range(M) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N + 1)
    cnt = 0
    for i in range(1, N +1) :
        if not visited[i] :
            dfs(i)
            cnt += 1

    print(f'#{test_case}' , cnt)
T = 10

for test_case in range ( 1, T + 1) :

    Start, End = 0, 99  # 출발 지점 , 도착 지점
    V = 100     # 노드 개수
    tc, E = map(int, input().split())   # test_case, 간선 수
    graph = [[] for _ in range (V)]     # 인접 행렬 생성 (graph 만들기)
    dfs_visited = [False] * (V)         # visited 행렬 만들기 (0부터 시작해서 V로 설정)
    graph_lst = list(map(int,input().split()))  # graph 만들기 위한 list input값 받기
    #print(len(graph_lst))
    for i in range(E) :     # 그래프 만들기
        a = graph_lst[i * 2]
        b = graph_lst[i * 2 + 1]
        graph[a].append(b)      # 그래프에 내가 가는 길 넣어!
    #print(graph)

    way = []
    def DFS(start):

        dfs_visited[start] = True   # 방문해
        way.append(start)       # 간 길 저장

        for i in graph[start] :     #   그래프 포문 돌아
            if not dfs_visited[i] :     # 방문 안했으면 DFS 앵콜
                DFS(i)


        return way

    WAY = DFS(Start)    # DFS로 탐색한 경로 받아!
    #print(WAY)
    for i in range (len(WAY)) :
        #print(WAY[i])
        if WAY[i] == End :      # 그 경로에 갔었으면 1출력
            result = 1
            #print(WAY[i], result, End)
            break
        else :
            result = 0


    print(f'#{test_case} {result}')


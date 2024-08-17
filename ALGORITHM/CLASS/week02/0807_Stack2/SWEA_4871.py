T = int(input())

for test_case in range ( 1, T + 1) :

    V, E = map(int, input().split())
    graph = [[] for _ in range (V + 1)]
    dfs_visited = [False] * (V + 1)

    for i in range(E) :
        a, b = map(int, input().split())
        graph[a].append(b)
    Start, End = map(int, input().split())
    #print(graph)

    way = []
    def DFS(start):

        dfs_visited[start] = True
        way.append(start)

        for i in graph[start] :
            if not dfs_visited[i] :
                DFS(i)


        return way

    WAY = DFS(Start)
    #print(WAY)
    for i in range (len(WAY)) :
        #print(WAY[i])
        if WAY[i] == End :
            result = 1
            #print(WAY[i], result, End)
            break
        else :
            result = 0


    print(f'#{test_case} {result}')


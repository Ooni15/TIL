from collections import deque

def bfs_node (Graph, Start, End) :

    cost = 0
    queue = deque([(Start, cost)])
    bfs_visited[Start] = True
    #print(queue)
    while queue :
        way = queue.popleft()
        if way[0] == End :
            return way[1]

        for i in Graph[way[0]] :
            # print(Graph[way[0]])
            # print(i)
            # print(bfs_visited)
            if not bfs_visited[i] :
                cost = way[1] + 1
                queue.append((i, cost))
                #print(queue)
                bfs_visited[i] = True
        if len(queue) == 0 :
            return 0


T = int(input())

for test_case in range(1, T + 1 ) :

    V, E = map(int,input().split())
    graph = [[] for _ in range (V + 1)]
    bfs_visited = [False] * (V + 1)

    for i in range (E) :
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    S, G = map(int,input().split())

    print(f'#{test_case}' , bfs_node(graph, S, G))

    '''
1
6 5
1 4
1 3
2 3
2 5
4 6
1 6 
    '''
from collections import deque
N , M, V = map(int,input().split())

dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

graph = [[] for _ in range (N+1)]

for i in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph :
    i.sort()

def dfs(start) :

    dfs_visited[start] = True
    print(start, end = ' ')

    for i in graph[start] :
        if not dfs_visited[i]:
            dfs(i)

def bfs(start) :

    queue = deque([start])

    bfs_visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v] :
            if not bfs_visited[i] :
                queue.append(i)
                bfs_visited[i] = True

    
dfs(V)
print()
bfs(V)
from collections import deque

# dfs
def dfs(start):

    visited_dfs[start] = True
    print(start,end = ' ')

    for node in graph[start]:
        if not visited_dfs[node]:
            dfs(node)

# bfs
def bfs(start):

    queue = deque([start])
    visited_bfs[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for node in graph[v]:
            if not visited_bfs[node]:
                queue.append(node)
                visited_bfs[node] = True


# main
N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

dfs(V)
print()
bfs(V)
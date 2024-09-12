from collections import deque

def bfs(start) :

    global cnt
    queue = deque([start])
    visited[start] = True

    while queue :
        vertex = queue.popleft()
        for v in graph[vertex] :
            if not visited[v] :
                queue.append(v)
                visited[v] = True
                cnt += 1



# main
V = int(input())
E = int(input())
graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
cnt = 0

for i in range(E) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
print(cnt)
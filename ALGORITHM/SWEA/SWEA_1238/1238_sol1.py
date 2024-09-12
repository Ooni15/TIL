from collections import deque

def bfs(start, level) :

    queue = deque([(start, level)])
    level = 1
    visited[start] = level


    while queue :
        info = queue.popleft()
        start , cost = info[0], info[1]

        for V in graph[start] :
            if not visited[V] :
                queue.append((V, cost + 1))
                visited[V] = cost + 1

# main
T = 10

for test_case in range (1, T + 1) :

    N, S = map(int,input().split())
    arr = list(map(int,input().split()))
    graph = [[] for _ in range (100 + 1)]
    visited = [0] * (100 + 1)


    for i in range (N // 2) :
        a, b = arr[2 * i], arr[2 * i + 1]
        graph[a].append(b)

    bfs(S, 1)
    max_index = 0
    max_visited = max(visited)

    for i in range (1, 100 + 1) :
        if visited[i] == max_visited :
            if max_index < i :
                max_index = i


    print(f'#{test_case} {max_index}')

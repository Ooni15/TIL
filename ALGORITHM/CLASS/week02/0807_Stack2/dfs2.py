def DFS (s, V) :
    visited = [0] * (V + 1)
    stack = []
    visited[s] = 1
    v = s
    while True :
        for w in adjL[v] :      # v에 인접하고, 방문안한 w가 있으면
            if visited[w] == 0:
                stack.append(v)     # push(v) 현재 정점을 push하고
                v = w               # w에 방문
                visited[w]          # w에 방문 표시
                break               # v부터 다시 탐색
        else :
            if stack :  # 이전 갈림길을 스택에서 꺼내서.. if TOP > -1
                v = stack.pop()
            else :      # 되돌아 갈 곳이 없으면
                break

 T = int(input())
 for test_case in range (1, T + 1) :






# from collections import deque
# N, M, v = map(int,input().split())
# graph = [[] for _ in range(N+1)]
# dfs_visited = [False] * (N+1)
# bfs_visited = [False] * (N+1)
#
# for i in range (M) :
#     a, b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# for i in graph :
#     i.sort()
#
# def dfs(start) :
#
#     dfs_visited[start] = True
#     print(start, end = ' ')
#
#     for i in graph[start] :
#         if not dfs_visited[i] :
#             dfs(i)
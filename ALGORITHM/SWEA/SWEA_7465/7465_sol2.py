import sys
sys.stdin  = open("input.txt", "r")

def dfs(start) :

    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

# main
T = int(input())

for test_case in range (1, T + 1) :

    N , M = map(int,input().split())
    graph = [[] for _ in range (N + 1)]
    visited = [False] * (N + 1)
    cnt = 0     # 무리의 개수

    # 그래프 만들기
    for i in range (M) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # dfs 다 돌기
    for i in range (1, N + 1) :
        if not visited[i] :
            dfs(i)
            cnt += 1        # 무리 개수 count

    print(f'#{test_case} {cnt}')



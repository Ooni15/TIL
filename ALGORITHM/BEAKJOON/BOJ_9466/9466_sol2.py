# Recursion Error
T = int(input())

def dfs(start):

    global cycle, team


    visited[start] = True   # 방문하면 visited True
    cycle.append(start)     # cycle에 넣어줘
    next = graph[start]     # 다음에 올 친구를 먼저 찾아
# 시작점 친구랑 만나면 멈춰야해

    if visited[next]:
        if next in cycle:
            team += cycle[cycle.index(next):]
            return
    else :
        dfs(next)



for test_case in range(T):
    n = int(input())
    graph = [0] + list(map(int,input().split()))
    friends = [0] * (n+1)
    visited = [False] * (n + 1)
    team = []
    for i in range(1, n+1) :
        cycle = []
        if not visited[i]:
            dfs(i)

    print(n-len(team))

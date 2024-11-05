T = int(input())

def dfs(start):

    global cycle, team

    while True:
        visited[start] = True   # 방문하면 visited True
        cycle.append(start)     # cycle에 넣어줘
        next = graph[start]     # 다음에 올 친구를 먼저 찾아
    # 시작점 친구랑 만나면 멈춰야해

        if visited[next]:       # 다음에 올 친구가 visited가 되어있다?
            if next in cycle:   # 그 친구가 cycle에 있는지 검사 => 1. 있으면 친구,
                team += cycle[cycle.index(next):]   # 친구면 team에 그 인덱스들 다 넣어줌
                return
            else:               # => 2. 없으면 앞에 애들 싹다 바보
                return

        if not visited[next] :  # 방문 안했으면
            start = next        # start에 next 넣고 돌려


    # if visited[next]:
    #     if next in cycle:
    #         team += cycle[cycle.index(next):]
    #     return
    # else :
    #     dfs(next)



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



T = int(input())

for test_case in range (1, T + 1) :
    N , M = map(int,input().split())
    graph_arr = list(map(int,input().split()))
    new_lst = [[] for _ in range ( N + 1 )]
    visited = [False] * (N + 1)

    for i in range (M) :
        a, b = graph_arr[2 * i], graph_arr[2 * i + 1]
        visited[a], visited[b] = True, True

        if a < b :
            new_lst[a].append(b)
        elif a > b :
            new_lst[b].append(a)
        else :
            continue
    total = 0
    only = N - sum(visited[1:])
    for item in (new_lst) :
        if len(item) >= 1 :
            total += 1
    print(new_lst)
    print(f'#{test_case} {total + only}')
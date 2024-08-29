def DFS (current, visit, result, N) :

    if len(current) == N :
        result.append(current[:])
        return

    for i in range(N) :
        if not visit[i] :
            visit[i] = True
            current.append(i)

            DFS(current, visit, result, N)

            visit[i] = False
            current.pop()

    return result

# main
T = int(input())
for test_case in range (1, T + 1) :
    N = int(input())
    danger = [list(map(int,input().split())) for _ in range (N)]
    print(danger)


    result = []
    visited = [False] * N
    print(DFS([], visited, result , N))
    M = len(result)         # 총 나오는 갯수
    min_case_sum = max(max(danger))
    for case in result :
        case_sum = 0
        for i in range (len(case) - 1) :
            a = case[i]
            b = case[i + 1]
            case_sum += danger[a][b]
        if min_case_sum > case_sum :
            min_case_sum = case_sum


print(f'#{test_case}', min_case_sum)



'''
1
3
0 7 2
6 0 5
4 3 0
'''


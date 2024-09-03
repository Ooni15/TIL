def dfs(start, level) :
    global result, number

    if level == N :
        result = max(result, int("".join(number)))
        return

    for i in range (start, len(number) - 1 ) :      # 마지막 놈은 안바꿔도 돼
        for j in range(i + 1, len(number)) :      # 바꿈 당할 놈
            if int(number[i]) <= int(number[j]) :
                number[i], number[j] = number[j], number[i]
                dfs(i, level + 1)
                number[i], number[j] = number[j], number[i]

            if i == len(number) - 2 and j == len(number) - 1 :
                number[i], number[j] = number[j], number[i]
                dfs(i, level + 1)
                number[i], number[j] = number[j], number[i]

T = int(input())

for test_case in range (1, T + 1) :

    number_str, N = map(str,input().split())       # N이 len 2이면 10인거임
    number = list(number_str)
    # 이래도 되낭?
    result = 0
    N = int(N)
    dfs(0,0)

    print(f'#{test_case} {result}')
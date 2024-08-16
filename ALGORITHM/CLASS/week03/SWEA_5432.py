T = int(input())

for test_case in range (1, T + 1) :

    arr = list(map(str,input()))
    #print(arr)
    stack = []
    pipe = []
    razor = []
    pipes = []
    for i in range (len(arr)) :
        if arr[i] == '(' :
            stack.append(i)

        elif arr[i] == ')' :
            pipe.append(stack.pop())
            pipe.append(i)

    k = 0
    cnt = 0 # 조각난 거 갯수
    while k + 2 < len(pipe) + 1 :
        if pipe[k] == pipe[k + 1] - 1 :
            razor.append(pipe[k])
            k += 2
        else :
            pipes.append([pipe[k], pipe[k+ 1]])
            k += 2

    # print(razor)
    # print(pipes)

    for pipi in (pipes) :
        for j in range (pipi[0], pipi[1] + 1) :
            if j in razor :
                cnt += 1

    result = cnt + len(pipes)
    print(f'#{test_case}', result)
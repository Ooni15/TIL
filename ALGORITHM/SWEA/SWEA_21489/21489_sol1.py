def DFS_sum (index, current, current_sum)
    global cnt
    if len(current) == N :
        if current_sum == K :
            cnt += 1
        return

    for i in range(index, len(arr)) :
        current.append(arr[i])      # 현재 인덱스의 원소를 부분집합에 추가
        DFS_sum(i + 1, current, current_sum + arr[i])   # 다음 원소 탐색
        current.pop()




T = int(input())

for test_case in range(1 , T + 1) :
    N, K = map(int,input().split())
    cnt = 0

    arr = list(range(1, 13))
    DFS_sum(0, [], 0)
    print(f'#{test_case}', cnt)
def DFS(index, current_sum) :
    global cnt

    if index == N :
        return

    current_sum += arr[index]

    if current_sum == S :
        cnt += 1

    # 합이 나를 포함 할 때
    DFS(index + 1, current_sum)

    # 합이 나를 포함 안할 때
    DFS(index + 1, current_sum - arr[index])

N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
DFS(0, 0)

print(cnt)


def DFS(index, current, result) :
    if current :        # 공집합 제외
        result.append(current[:])

    for i in range(index, N) :
        current.append(arr[i])

        DFS(i + 1, current, result)

        # 백트래킹
        current.pop()

N, S = map(int, input().split())
arr = list(map(int, input().split()))

result = []
DFS(0, [], result)
cnt = 0
for case in result :
    if sum(case) == S :
        cnt += 1

print(cnt)


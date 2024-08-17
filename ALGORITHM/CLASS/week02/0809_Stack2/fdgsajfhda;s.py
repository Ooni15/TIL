def dfs(l, n, arr, k, visited, start, suum):
    global cnt
    if suum > k:
        return
    if l == n:
        if suum == k:
            cnt += 1
        return
    else:
        for i in range(start, 13):
            if visited[i] == 0:
                arr[l] = i
                visited[i] = 1
                dfs(l + 1, n, arr, k, visited, i + 1, suum + i)
                visited[i] = 0


T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    cnt = 0
    visited = [0] * 13
    arr = [0] * n
    dfs(0, n, arr, k, visited, 1, 0)
    print(f'#{t + 1} {cnt}')

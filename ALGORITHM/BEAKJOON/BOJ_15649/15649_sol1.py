N, M = map(int,input().split())

arr = []
visited = [False] * (N + 1)

def recur(num, level) :

    if level == M :
        print(*arr)

        return

    for i in range(1, num + 1) :
        if not visited[i] :
            arr.append(i)
            visited[i] = True
            recur(num, level + 1)
            arr.pop()
            visited[i] = False

recur(N ,0)

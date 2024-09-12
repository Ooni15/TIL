N, M = map(int,input().split())
arr = []
lst = []
visited = [False] * (N + 1)
def recur(now, level) :

    if level == M :
        print(*arr)

        return

    for i in range (now, N + 1) :
        arr.append(i)
        recur(i + 1, level + 1)
        arr.pop()

recur(1, 0)


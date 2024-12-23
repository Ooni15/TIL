from collections import deque

N, K = map(int,input().split())
visited = [-1] * 100001
cnt = [0] * 100001

visited[N] = 0
cnt[N] = 1

queue = deque([N])


while queue:
    now = queue.popleft()

    nexts = [now + 1, now -1, now * 2]

    for next in nexts:
        if 0 <= next <= 100000:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                cnt[next] = cnt[now]
                queue.append(next)
            elif visited[next] == visited[now] + 1:
                cnt[next] += cnt[now]

print(visited[K])
print(cnt[K])


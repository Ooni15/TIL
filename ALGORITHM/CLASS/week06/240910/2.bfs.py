# page31. 연습문제2
import sys
sys.stdin = open("../../../../../../강의자료/algorithm/20240910_그래프기본/graph.txt", "r")


def bfs(node):
    q = [node]

    while q:
        now = q.pop(0)

        print(now, end=' ')  # 현재 노드 출력

        for next_node in graph[now]:
            if visited[next_node]:
                continue

            visited[next_node] = 1
            q.append(next_node)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited[1] = 1
bfs(1)

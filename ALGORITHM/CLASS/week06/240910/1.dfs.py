# page25. 연습문제1
import sys
sys.stdin = open("../../../../../../강의자료/algorithm/20240910_그래프기본/graph.txt", "r")


def dfs(node):
    print(node, end=' ')  # 현재 노드 출력

    # 갈 수 있는 노드들을 탐색
    for next_node in graph[node]:
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited[1] = 1
dfs(1)

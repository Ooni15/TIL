from pprint import pprint
V, E = map(int,input().split())

# 간선정보
data = list(map(int, input().split()))
print(data)

def DFS(start) :
    # 방문 기록
    visited[start] = 1
    # 방문한 노드를 출력
    print(start, end = ' ')

    # 다음으로 조사가 가능한 노드 찾기
    for next in range(1, V + 1) :
        # 현재 노드에 인접해 있고 방문한 적이 없는 곳
        if matrix[start][next] == 1 and visited[next] == 0:
            # 또 다시 탐색 시작
            DFS(next)

'''
DFS 재귀함수의 종료 조건
1. 암묵적인 종료 조건
    - 현재 노드에서 더 이상 방문할 수 있는 인접 노드가 없을 때 함수 종료
    - for 반복에서 모든 노드를 검사 했지만 조건을 만족하는 노드가 없다면 종료
'''
'''
동작 과정
1. DFS(1) 호출
2. 1번 노드 방문 표시 및 출력
3. 1번 
'''
# 인접 행렬 만들기
matrix = [[0] * (V + 1) for _ in range (V + 1)]

for i in range(E) :
    n1 = data[i * 2]
    n2 = data[i * 2 + 1]
    matrix[n1][n2] = 1
    matrix[n2][n1] = 1

pprint(matrix)
DFS(1)
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
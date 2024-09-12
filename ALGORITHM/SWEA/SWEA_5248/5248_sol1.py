# import sys
# sys.stdin = open("input.txt", "r")

# make set
def make_set(n) :
    p = [i for i in range (n + 1)]  # 각 원소의 부모를 자기 잔으로 초기화
    r = [0] * (n + 1)     # 랭크 만들어주기
    return p,r

# find(x)
def rang(x) :
    # 원소의 부모가 자기 자신이다. == 자기가 그 그룹의 다표자
    if parents[x] == x :
        return x

    # 경로 압축 (path compression)을 통해 부모를 루트로 설정
    parents[x] = rang(parents[x])
    return parents[x]

# union
def union(x, y) :
    root_x = rang(x)
    root_y = rang(y)    # 엄마 불러

    if root_x == root_y :   # 이미 같은 집합이면 끝
        return

    # rank를 비교하여 더 작은 트리를 큰 트리의 밑에 병합
    if ranks[root_x] > ranks[root_y] :
        parents[root_y] = root_x
    elif ranks[root_x] < ranks[root_y] :
        parents[root_x] = root_y
    else :
        # rank가 같으면 한쪽을 다른 쪽 아래로 병합하고 rank를 증가시킴
        parents[root_y] = root_x
        ranks[root_x] += 1

# main
T = int(input())

for test_case in range (1, T + 1) :
    N , M = map(int,input().split())
    graph_arr = list(map(int,input().split()))

    parents, ranks = make_set(N)

    for i in range (M) :
        a, b = graph_arr[2 * i], graph_arr[2 * i + 1]
        union(a, b)


    # 최종적으로 다시 저장해줘함! 안그러면 중간에 호출한 애들은 새엄마로 못감
    for i in range (1 , N + 1) :
        rang(i)

    # print(parents)
    # print(f'#{test_case} {len(set(parents)) - 1}')
    print(f'#{test_case} {len(set(parents[1:]))}')



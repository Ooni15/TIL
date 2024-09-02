T = 10
def in_order(node):
    if node == 0 :
        return


    in_order(left[node])
    print(word[node], end = '')      # 여기면 중위 순회
    in_order(right[node])
    # print(node, end=' ')      # 여기면 후위


for test_case in range (1, T + 1) :
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    # 인접행렬 만들기
    word = [0] * (N+1)
    left = [0] * (N + 1)  # 부모를 인덱스로 왼쪽자식번호 저장
    right = [0] * (N + 1)  # 오른쪽 자식 번호를 저장할 리스트
    par = [0] * (N + 1)  # 자식을 인덱스로 부모 저장
    for item in arr :
        parent = int(item[0])
        word[parent] = item[1]
        if len(item) == 4 :
            left[parent] = int(item[2])      # 왼쪽에 넣어버령
            right[parent] = int(item[3])     # 오른쪽~
            par[left[parent]] = parent          # 넣은거 오마니 품으로 넣어주기
            par[right[parent]] = parent
        elif len(item) == 3 :
            left[parent] = int(item[2])      # 다시 왼쪽~
            par[left[parent]] = parent
        else :
            continue

    print(f'#{test_case}', end=' ')
    in_order(1)
    print()
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    w_lst = list(map(int, list(input().split())))  # 화물의 무게
    t_lst = list(map(int, list(input().split())))  # 트럭의 적재용량
    w_lst.sort()
    t_lst.sort()

    total = 0
    while N and M:
        if w_lst[N - 1] <= t_lst[M - 1]:
            total += w_lst[N - 1]
            N -= 1
            M -= 1
        elif w_lst[N - 1] > t_lst[M - 1]:
            N -= 1

    print(f'#{tc} {total}')
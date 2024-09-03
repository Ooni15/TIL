T = int(input())

for test_case in range( 1, T + 1) :
    N, M = map(int, input().split())    # N : 컨테이너 수, M : 트럭 수
    container = list(map(int,input().split()))
    truck = list(map(int, input().split()))

    container.sort(reverse=True)        # 큰 놈 앞으로 오게
    truck.sort(reverse=True)
    total = 0

    for i in range (M) :
        for j in range (N) :
            if container[j] != 0 and truck[i] >= container[j] :   # 트럭 자리 있으면
                total += container[j]       # 내가 챙긴 컨테이너 수 세기
                container[j] = 0            # 챙긴거는 0으로
                break


    print(f'#{test_case}', total)
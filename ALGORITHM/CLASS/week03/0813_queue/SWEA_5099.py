from collections import deque
T = int(input())

for test_case in range (1, T + 1) :

    N, M = map(int,input().split())
    arr = [0] + list(map(int,input().split()))

    queue = deque()

    for i in range (N + 1) :    # 0 부터 3까지 넣어
        queue.append((i,arr[i]))    # 인덱스와 같이 저장 (인덱스, 배열 값)

    test = queue.popleft() # 0번 인덱스 제거
    idx = N + 1
    while queue :

        for i in range(N) : # 3번
            a = queue.popleft()
            if idx < M + 1 :        # 남은 피자가 있다면
                if a[1] == 1 :         # 값이 1이 남으면 화덕 빈자리에 새로운 피자 추가
                    queue.append((idx,arr[idx]))
                    idx += 1        # 피자 인덱스 추가
                else :
                    queue.append((a[0],a[1]//2))      # 1 아니면 계속 화덕에서 돌려

            else :                  # 남은 피자가 없을 때
                if a[1] == 1 :         # 피자 다 녹았으면 일단 넘겨 (popleft상태)
                    if len(queue) == 1:
                        break
                else :
                    queue.append((a[0],a[1]//2))
                    if len(queue) == 1:
                        break
        if len(queue) == 1:
            break

    print(f'#{test_case}', queue[0][0])



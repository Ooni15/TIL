
from collections import deque

T = 10

for test_case in range(1, T + 1):
    tc = int(input())
    queue = deque()
    arr = list(map(int, input().split()))

    # 큐를 초기화
    for i in range(len(arr)):
        queue.append(arr[i])

    # 사이클을 돌리며 마지막 숫자가 0이 될 때까지 반복
    while True:
        for i in range(1, 6):  # 1에서 5까지 감소 / 한 사이클
            a = queue.popleft()
            if a - i <= 0:
                queue.append(0)
                check = 1
                break
            queue.append(a - i)
        if queue[-1] == 0:  # 큐의 마지막 요소가 0이면 루프 종료
            break

    # 결과 출력
    print(f'#{tc}', *queue)

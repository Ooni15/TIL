# from collections import deque
# # main
# T = int(input())
# for test_case in range(1, T + 1) :
#
#     N, M = map(int,input().split())
#     arr = list(map(int,input().split()))
#
#     queue = deque()     # queue 생성
#     for i in range(N) :     # queue 받은 list 값 넣기
#         queue.append(arr[i])
#
#     for i in range(M) :
#         a = queue.popleft()     # 순환 시키기
#         queue.append(a)
#
#     print(f'#{test_case}', queue.popleft())     # 맨 앞 출력


T = int(input())

for test_case in range(1, T + 1) :

    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    q = [0] * N * M     # queue에 들어갈 수 있는 값만큼 size 만들기
    front = -1
    rear = -1

    for i in range (N) :    # queue에 arr 값 넣기
        rear += 1
        q[rear] = arr[i]

    for i in range (M) :    # front 1개씩 올리고 -> 그 해당 값 큐에 넣기
        front += 1
        a = q[front]
        rear += 1
        q[rear] = a

    front += 1  # 최종 값 확인을 위해 front 1 추가
    print(f'#{test_case}',q[front])

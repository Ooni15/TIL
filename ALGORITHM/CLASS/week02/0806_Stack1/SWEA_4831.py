# arr 내에 n 보다 작은 값 중 가장 큰 수 반환
def min_max(n, arr) :

    min_arr = []
    for i in range(len(arr)) :
        if arr[i] < n :
            min_arr.append(arr[i])  # arr 내의 n보다 작은 값 저장
    max_val = min_arr[0]
    for i in range(len(min_arr)) :  # 작은 값 중 가장 큰 값 저장
        if max_val < min_arr[i] :
            max_val = min_arr[i]

    return max_val

T = int(input())

for test_case in range (1, T + 1) :

    K, N , M = map(int, input().split())
    charging = list(map(int,input().split()))

    # 현재 위치
    now = 0  # 시작 위치 0
    cnt = 0  # 결과 값인 카운트
    while now + K < N  :        # 마지막 애들 카운트 안되게 N - 1 까지
        if now + K in charging :    # K번 간 지점에 충전소가 있으면
            cnt += 1    # 충전 횟수
            now += K    # 현재 위치를 K번 이동한 위치로 변경
            #print(now)
        elif now + K not in charging :  # K번 간 지점에 충전소가 없으면
            new_k = min_max(now + K, charging)  # 이전에 가까운 충전소 찾기
            #print(now + K, new_k)
            if new_k == now :   # 찾은 충전소가 이전에 들린 곳이면 0
                cnt = 0
                break
            cnt += 1
            now = new_k # 충전소로 현재 위치 변경

    if now + K >= N :        # 마지막 충전 후 도착할 수 있는지 확인
        print(f'#{test_case} {cnt}')
    else :
        print(f'#{test_case}', 0)   # 도착하지 못하면 0





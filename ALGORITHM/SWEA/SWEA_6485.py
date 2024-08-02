T = int(input())

for test_case in range (1, T + 1) :

    count_number = [0] * 5001   # 5001개의 배열 생성
    N = int(input())    # 노선 갯수
    Line = [list(map(int,input().split())) for _ in range (N)]  # 노선 범위 [[A1, B1], [A2, B2]]
    P = int(input())    # 정류장 개수
    bus_station = [0] * P   # 버스 정류장 번호 리스트
    for i in range (P) :
        bus_station[i] = int(input())

    for i in range(N) :   # 배열 행 기준 순회
        for k in range (Line[i][0], Line[i][1] + 1 ) :  # 노선 내 범위 하나씩 더하기
            count_number[k] += 1    # 버스 정류장 번호와 count_number 인덱스 동일하게 만들어 count

    result = [0] * P
    for i in range(P) :     # 버스 정류장 번호 리스트 순회
        result[i] = count_number[bus_station[i]]    # 버스 정류장 번호에 맞는 count 넣어주기


    print(f'#{test_case}', *result)
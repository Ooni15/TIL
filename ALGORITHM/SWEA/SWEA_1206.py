# T = 10
# for test_case in range(1,1+T) :
#
#     N = int(input())
#     building_arr = list(map(int,input().split()))
#     view_arr = [0]*4 # 4개의 건물의 조망 확인
#     view_cnt = 0
#     #print(len(building_arr))
#
#     def mini(arr):
#
#         mini = 255  # 건물 최대 높이 255
#         for i in range(len(arr)) :
#             if mini > arr[i] :
#                 mini = arr[i]
#
#         return mini
#
#
#     for i in range(2,N-2) :
#
#         view_arr[0] = building_arr[i] - building_arr[i - 2]
#         view_arr[1] = building_arr[i] - building_arr[i - 1]
#         view_arr[2] = building_arr[i] - building_arr[i + 1]
#         view_arr[3] = building_arr[i] - building_arr[i + 2]
#
#         if (view_arr[0]>=0) & (view_arr[1]>=0) & (view_arr[2]>=0)& (view_arr[3]>=0):
#
#             view_cnt += mini(view_arr)
#
#
#
#     print(f'#{test_case} {view_cnt}')

## 강사님 풀이
for tc in range(1, 11) :
    N = int(input())
    arr = list(map(int,input().split()))

    result = 0
    for i in range(2, N-2) : # 양 끝 2자리 무시
        # 현재 조사 대상의 높이
        tmp = arr[i]
        # 양쪽 두 칸씩 검사
        for j in range(i-2, i+3) :
            if i == j : # 나랑 비교할 필요 없음
                continue

            # 조사 대상의 양 옆보다 크고
            # 그 둘의 차이가 조망권 보다 작으면
            # 단축 평가로, 양쪽 조망권이 확보 되었고,
            # AND 현재 검사 대상의 높이와 양쪽 두 칸과의 차가 더 작으면

            if arr[i] > arr[j] and tmp > arr[i] - arr[j] :
                tmp = arr[i] - arr[j] # 조망권이 확보된 세대 갯수로 갱신
            # 나 보다 양 옆 건물이 같거나 큰 경우가 한번이라도 있으면,
            elif arr[i] <= arr[j] : # 조망권이 확보되지 않았을 경우
                # tmp  갱신할 필요 X
                break # 그 다음 건물로 넘어가기

        else :
            result += tmp

    print(f'#{tc} {result}')
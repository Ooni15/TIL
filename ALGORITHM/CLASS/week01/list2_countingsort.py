# DATA = [0, 4, 1, 3, 1, 2, 4,1 ]
# COUNTS = [0] * 5  # DATA가 0-4까지의 정수
#
# N = len(DATA)     # DATA의 크기
# TEMP = [0] * N    # 정렬 결과 저장
#
# # 1단계 : DATA 원소 별 개수 세기
# for x in DATA :     # DATA의 원소 x를 가져와서 COUNT[x]에 개수 기록
#     COUNTS[x] += 1
#
# # 2 단계 : 각 숫자까지의 누적 개수 구하기
# for i in range(1, 5) : # COUNT[0]~ COUNT[4]까지 누적
#     COUNTS[i] += COUNTS[i - 1]
#
# # 3 단계 : DATA의 맨 뒤부터 TEMP에 자리 잡기
# for i in range(N-1, -1, -1) :
#     COUNTS[DATA[i]] -= 1    # 누적 개수 1개 감소
#     TEMP[COUNTS[DATA[i]]] = DATA[i]
#
#
# print(*TEMP)



def counting_sort(arr, k) :
    """
    input_arr : 입력 배열 ( 0 -> k)
    counting_arr : 카운팅 배열 
    k는 데이터의 개수가 아닌, 데이터 원소 범위
    """
    counting_arr = [0] * (k+1) # 카운팅 배열 // k는 데이터의 원소 범위

    # 1. counting_arr에 input_arr 내 원소의 빈도 수 담기
    for i in range(len(arr)) : # input_arr 만큼 순회 // input_arr의 원소 하나씩 꺼내기
        counting_arr[arr[i]] += 1 # counting_arr[0], counting_arr[4]

    # 2. 누적(counting_arr) 업데이트 -> 내 앞에 몇개?
    for i in range(1,len(counting_arr)) :
        counting_arr[i] += counting_arr[i-1] # counting_arr[1] = counting_arr[1] + counting_arr[0]

    # 3. result_arr 초기화  : 정렬된 결과
    result_arr = [-1] * len(arr)

    # 4. result_arr에 정렬하기 (counting_arr를 참조할 것 이다.) [0, 4, 1, 3, 1, 2, 4,1 ]
    for i in arr : # arr는 순회 가능한 iterable한 객체 -> collection
        counting_arr[i] -= 1 # 0, 4, 1, 3 ... : counting_arr의 해당 원소 값 하나 줄인다.
        result_arr[counting_arr[i]] = i # result_arr에 counting_arr의 해당 요소를 넣는다

    return result_arr

input_arr = [0, 4, 1, 3, 1, 2, 4,1 ]  # 정렬할 target
print(counting_sort(input_arr, 5))
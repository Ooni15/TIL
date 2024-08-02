# 딕셔너리 생성
change_number = {
    'ZRO' : 0,
    'ONE' : 1,
    'TWO' : 2,
    'THR' : 3,
    'FOR' : 4,
    'FIV' : 5,
    'SIX' : 6,
    'SVN' : 7,
    'EGT' : 8,
    'NIN' : 9
 }

# 영어를 숫자로 변경하기
def to_int (arr, N) :

    num_arr = [0] * N
    for i in range(N) :
        num_arr[i] = change_number[arr[i]]  # dictionary key값에 해당하는 값 추가

    return num_arr

# 선택 정렬하기
def selection_sort(arr, N) :


    for i in range(N-1) :   # 하나는 안해도 돼
        min_idx = i         # 최솟값 위치를 기준으로 가정
        for j in range(i+1, N) : # 남은 원소에 대해 실제 최솟값
            if arr[min_idx] > arr[j] :
                min_idx = j         # 구간의 최솟값으로 이동

            # 구간의 최솟값을 기준위치로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

def to_ENG (arr, N) :

    eng_arr = [0] * N
    for i in range(N) :
        for key, value in change_number.items() :   # 딕셔너리의 key값과  value값 순회
            if arr[i] == value :    # 배열 값이 value와 동일하다면 key 값 반환
                eng_arr[i] = key

    return eng_arr



T = int(input())

for test_case in range(1, 1 + T) :

    tc, N = map(str,input().split())
    N = int(N)
    lst = list(map(str,input().split()))  # input 받기
    # 영어 -> 숫자
    num_lst = to_int(lst, N)
    # 숫자 정렬
    sort_lst = selection_sort(num_lst, N)
    # 숫자 -> 영어
    eng_lst = to_ENG(sort_lst, N)

    print(f'#{test_case}')
    print(*eng_lst)

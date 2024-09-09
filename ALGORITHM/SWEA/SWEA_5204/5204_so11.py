def merge_sort(m) :
    # 리스트 길이가 1이면 이미 정렬된 상태이므로 그대로 반환
    if len(m) == 1 :
        return m

    # 리스트를 절반으로 나누기 위해 중간 인덱스를 계산
    mid = len(m) // 2
    left = m[:mid]      # 리스트의 앞쪽 절반
    right = m[mid:]     # 리스트이 뒤쪽 절반

    # 재귀적으로 왼쪽 부분과 오른쪽 부분을 정렬
    left = merge_sort(left)
    right = merge_sort(right)

    # 두 개의 정렬된 리스트를 병합하여 반환  -> 이 횟수를 구해주면 되는거 아닌가
    return merge(left, right)

def merge(left, right) :
    global cnt
    # 두 리스트를 병합할 결과 리스트를 초기화
    result = [0] * (len(left) + len(right))
    l = r = 0       # 왼쪽 리스트와 오른쪽 리스트의 인덱스


    # 두 리스트를 순차적으로 비교하여 작은 값을 결과 리스트에 추가
    while l < len(left) and r < len(right) :
        if left[l] < right[r] :
            result[l + r] = left[l]
            l += 1
        else :
            result[l + r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 요소들을 결과 리스트에 추가
    while l < len(left) :
        result[l + r] = left[l]
        l += 1

    # 오른족 리스트에 남은 요소들을 결과 리스트에 추가
    while r < len(right) :
        result[l + r] = right[r]
        r += 1

    if right[-1] < left[-1] :
        cnt += 1

    return result


T = int(input())

for test_case in range (1, T + 1) :

    N = int(input())
    arr = list(map(int,input().split()))

    cnt = 0

    arr = merge_sort(arr)
    print(f'#{test_case} {arr[N//2]} {cnt}')
def selection_sort(arr, k) :
    for i in range(k-1) : # 주어진 구간에 대해... 기준 위치 i를 정하고
        min_idx = i     # 최솟값 위치를 기준으로 가정
        for j in range(i+1, k) :    # 남은 원소에 대해 실제 최솟값 위치 검색
            if arr[min_idx] > arr[j] :
                min_idx = j
            # 구간의 최솟값을 기준위치로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr[k-1]

# main
A = [2,7,5,3,4]
selection_sort(A, len(A))
print(A ) # [2, 3, 4, 5, 7]
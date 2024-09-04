def BubbleSort (arr) :
    N = len(arr)
    for i in range(N-1, 0 , -1) :
        for j in range(0, i) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def SelectionSort (arr) :

    N = len(arr)
    for i in range(N-1) :
        min_idx = i
        for j in range(i+1, N) :
            if arr[min_idx] > arr[j] :
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx] , arr[i]

    return arr

# main
T = int(input())

for test_case in range (1, T + 1) :

    N = int(input())
    lst = list(map(int, input().split()))

    result = SelectionSort(lst)

    print(f'#{test_case}', *result)

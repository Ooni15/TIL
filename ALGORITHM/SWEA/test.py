arr = [3, 3, 2, 4, 1]

def bubble_sort (arr) :

    N = len(arr)

    for i in range(N-1 , 0, -1 ) :
        for j in range (i) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort(arr))
arr1 = [0, 4, 1, 3, 1, 2, 4, 1]
def Counting_sort (arr) :

    max_val = arr1[0]
    for i in range(len(arr)) :
        if max_val < arr[i] :
            max_val = arr[i]

    count_arr = [0] * (1 + max_val)
    for i in range(len(arr)) :
        count_arr[arr[i]] += 1

    result = [-1] * len(arr)
    for i in range (1, len(count_arr)) :
        count_arr[i] += count_arr[i - 1]

    for i in arr :
        count_arr[i] -=1
        result[count_arr[i]] = i

    return result

print(Counting_sort(arr1))
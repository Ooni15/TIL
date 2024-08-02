def reverse_str (arr) :

    N = len(arr)
    new_arr = [0] * N
    for i in range(N//2 + 1) :
        new_arr[i], new_arr[N - 1 - i] = arr[N - 1 - i], arr[i]

    return new_arr

T = int(input())
for test_case in range(1, T+1) :

    lst = list(input())
    re_lst = (reverse_str(lst))

    if lst ==  re_lst :
        result = 1
    else :
        result = 0

    print(f'#{test_case} {result}')

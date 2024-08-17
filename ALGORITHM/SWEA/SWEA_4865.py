def Count (arr, X ) :
    cnt = 0
    for i in range(len(arr)) :
        if arr[i] == X :
            cnt += 1

    return cnt

def max_dict (dictionary) :

    max_value = 0
    for value in dictionary.values() :
        if max_value < value :
            max_value = value

    return max_value

# main
T = int(input())

for test_case in range (1, T + 1) :
    lst1 = list(map(str, input()))
    lst2 = list(map(str, input()))
    lst_1 = list(set(lst1))
    count_dct = dict()

    for i in range (len(lst_1)) :
        if lst_1[i] in lst2 :
            count_dct[lst_1[i]]=Count(lst2, lst_1[i])

    print(f'#{test_case} {max_dict(count_dct)}')

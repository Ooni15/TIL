def make_comb(index, result, m, z):

    if len(result) == L:      # 모음 1개 이상 자음 2개 이상
        if m >= 1 and z >=2:
        # 이새끼 언제 터트리지?
            print(result)
            return result

    for i in range(index + 1, M):
        if arr_sort[i] in m_lst:
            make_comb(i, result + arr_sort[i], m+1, z)

        else:
            make_comb(i, result+arr_sort[i], m, z+1)

# main
L, M = map(int, input().split())
arr = list(map(str,input().split()))
arr_sort = sorted(arr)

m_lst = ['a', 'e', 'i', 'o', 'u']
make_comb(-1, '', 0, 0)



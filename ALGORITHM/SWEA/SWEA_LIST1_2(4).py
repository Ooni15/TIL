T = int(input())

for test_case in range(1,T+1) :
    print(test_case)
    N = int(input())
    arr = list(map(int,input().strip()))
    print(test_case, arr)

    def mani(arr) :

        mani = 0
        for i in range(len(arr)) :
            if mani < arr[i] :
                mani = arr[i]

        return mani

    # main
    num_max = mani(arr)
    counts = [0] * (num_max + 1)

    for i in range (N) :
        counts[arr[i]] += 1

    print(f'#{test_case} {num_max} {counts[num_max]}')
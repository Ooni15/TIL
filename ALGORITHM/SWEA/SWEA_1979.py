T = int(input())


for test_case in range(1, T+1) :
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]


    def find_block(arr, K) :
        result = 0
        for i in range(len(arr)) :
            cnt = 0
            for j in range(len(arr)) :
                if arr[i][j] == 1:
                    cnt += 1
                    if j == len(arr) - 1:

                        if cnt == K :
                            result += 1
                else :
                    if cnt == K :
                        result += 1

                    cnt = 0

        return result


    def zip_block(arr) :

        lst = [[0]* len(arr) for _ in range (len(arr))]
        for i in range(len(arr)) :
            for j in range(len(arr)) :
                lst[i][j] = arr[j][i]

        return lst

    arr1 = zip_block(arr)
    answer = find_block(arr, K) + find_block(arr1, K)
    print(f'#{test_case} {answer}')
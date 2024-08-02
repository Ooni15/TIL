def destination (arr) :
    for i in range(len(arr)) :
        if arr[-1][i] == 2 :
            return i

def Ladder (arr, K) :

    i = len(arr) -1
    j = K

    while i > 0 :
        # 양 옆 확인

        if 0 < j < len(arr[0]) - 1 : # 첫 번째 열, 마지막 열 제외
            # 왼쪽 이동
            # print(i)
            if arr[i][j - 1] == 1:
                while j> 0 and arr[i][j-1] == 1 :
                    j -= 1
                i -= 1

            # 우측 이동
            elif arr[i][j + 1] == 1:
                while j < len(arr[0]) -1  and arr[i][j+1] == 1 :
                    j += 1
                i -= 1

            else :
                i -= 1

        elif j == 0 :  # 첫 번째 열
            if arr[i][j + 1] == 1:  # 오른쪽 확인
                while j < len(arr[0]) - 1 and arr[i][j + 1] == 1:  # 오른쪽 이동
                    j += 1
            i -= 1  # 위로 이동

        elif j == len(arr[0]) - 1:  # 마지막 열
            if arr[i][j - 1] == 1:  # 왼쪽 값 확인
                while j > 0 and arr[i][j - 1] == 1:  # 왼쪽 이동 조건
                    j -= 1
            i -= 1  # Move up



    return j

# main
T = 10

for test_case in range (1, T+1) :

    L = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    N = destination(ladder)
    print(f'#{L} {Ladder(ladder, N)}')



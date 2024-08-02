T = 10
for test_case in range (1, 1+ T) :
    N = int(input()) # N번 움직일거임
    lst = list(map(int,input().split()))

    #
    # def mini(arr):
    #
    #
    #     mini = 100  # 최대 길이 100
    #     for i in range(len(arr)):
    #         if mini > arr[i]:
    #             mini = arr[i]
    #
    #     return mini
    #
    # def mani(arr):
    #
    #     mani = 1  # 최소 길이 1
    #     for i in range(len(arr)):
    #         if mani < arr[i]:
    #             mani = arr[i]
    #
    #     return mani

    def bubble_sort(arr) :
        for i in range(len(arr) - 1, 0, -1):  # 각 구간의 끝 인덱스 i
            for j in range(i):  # 각 구간에서 두 개씩 비교할 때 왼쪽 원소의 인덱스 j
                if arr[j] > arr[j + 1]:  # 왼쪽 원소가 더 크면 교환
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    # main

    for i in range(N) :
        bubble_sort(lst)
        lst[len(lst)-1] = lst[len(lst) -1] - 1

        lst[0] = lst[0] + 1

    bubble_sort(lst)
    result = lst[len(lst)-1] - lst[0]

    print(f'#{test_case} {result}')
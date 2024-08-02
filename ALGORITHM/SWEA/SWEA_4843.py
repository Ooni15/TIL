# def selection_sort(arr, N) :
#
#
#     for i in range(N-1) :   # 하나는 안해도 돼
#         min_idx = i         # 최솟값 위치를 기준으로 가정
#         for j in range(i+1, N) : # 남은 원소에 대해 실제 최솟값
#             if arr[min_idx] > arr[j] :
#                 min_idx = j         # 구간의 최솟값으로 이동
#
#             # 구간의 최솟값을 기준위치로 이동
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#
#     return arr
# # main
# T = int(input())
#
# for test_case in range(1, T + 1) :
#
#     K = int(input())
#     numbers = list(map(int, input().split()))
#     numbers_sort = selection_sort(numbers, K)
#
#     lst_min = numbers_sort[0 : len(numbers)//2 + 1]
#     lst_max = numbers_sort[len(numbers)//2 + 1 :]
#
#     result = []
#     if len(numbers) % 2 == 1 :  # 홀수일 때
#         for i in range(len(numbers) // 2 + 2 ) :
#             result.append(numbers_sort[len(numbers) - 1 - i])
#             if (len(numbers) % 2 == 1) & (i == len(numbers) // 2 ):
#                 break
#             result.append(numbers_sort[i])
#     else :
#         for i in range(len(numbers) // 2 ) :
#             result.append(numbers_sort[len(numbers) - 1 - i])
#             result.append(numbers_sort[i])
#
#
#     print(f'#{test_case}', *result)
#

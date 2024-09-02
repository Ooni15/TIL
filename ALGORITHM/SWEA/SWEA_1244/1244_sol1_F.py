# def recur(lst , A) : # 숫자랑 교환횟수 받기
#
#     K = len(lst)
#     for _ in range (A) :         # A번 반복
#         for i in range(K - 1) :   # 기준 위치 i 정하기 마지막은 안해줘
#             # 정렬된 값이랑 동일하다면?
#             min_idx = i
#             pass
#
#
#
# def selection_sort(arr, k):
#     for i in range(k - 1):  # 주어진 구간에 대해... 기준 위치 i를 정하고
#         min_idx = i  # 최솟값 위치를 기준으로 가정
#         for j in range(i + 1, k):  # 남은 원소에 대해 실제 최솟값 위치 검색
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#             # 구간의 최솟값을 기준위치로 이동
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#
#     return arr[k - 1]
#
#
# T = int(input())
#
# for test_case in range (1, T + 1) :
#
#     number, N = map(list,input().split())       # N이 len 2이면 10인거임
#
#     # 이래도 되낭?
#     if len(N) == 2:
#         A = 10
#     else :
#         A = int(N[0])
#
#     for i in range(len(number)) :
#         number[i] = int(number[i])
#
#     print(number)

def prize(ls):
    money = 0
    for i in range(len(ls)):
        money += 10**(len(ls)-i-1)*int(ls[i])
    return money


T = int(input())
for tc in range(1, T+1):
    string, N = map(str, input().split())
    length = len(string)
    target = [string[i] for i in range(length)]
    combination = []
    path = []
    max_prize = 0
    maximum = prize(sorted(target, reverse=True))
    for i in range(length):
        for j in range(length):
            if i < j:
                combination.append([i, j])

    def exchange(x):
        global max_prize
        if x == int(N):
            new_target = target[:]
            for k in range(len(path)):
                if new_target[path[k][0]] != new_target[path[k][1]]:
                    new_target[path[k][0]], new_target[path[k][1]] = new_target[path[k][1]], new_target[path[k][0]]
            if prize(new_target) > max_prize:
                max_prize = prize(new_target)

            return
        for m in range(len(combination)):
            if target[combination[m][0]] != target[combination[m][1]]:
                path.append(combination[m])
            exchange(x+1)
            if max_prize == maximum:
                return
            if path:
                path.pop()

    exchange(0)
    print(f"#{tc} {max_prize}")
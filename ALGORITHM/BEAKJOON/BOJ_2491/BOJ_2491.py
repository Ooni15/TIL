# def plus(M, ARR) :
#     cnt = 0
#     max_cnt = 0
#     for i in range(M) :
#         if i == N-1 :
#             arr[i]
#         if arr[i] <= arr[i + 1] :
#             cnt += 1
#             if max_cnt < cnt :
#                 max_cnt = cnt
#         elif arr[i] >= arr[i+1] :
#             cnt = 0
#     pass
#
# def minus(M, ARR) :
#     pass

N = int(input())
arr = list(map(int,input().split()))

# plus(N, arr)
# minus(N,arr)
cnt = 1
max_cnt = 1
for i in range (N) :
    if i == N-1 :
        # if arr[i] >= arr[i - 1] :
        #     cnt += 1
        #     if max_cnt < cnt:
        #         max_cnt = cnt
        # else :
        #     cnt = 1
        break
    elif arr[i] <= arr [i + 1] :
        cnt += 1
        if max_cnt < cnt :
            max_cnt = cnt
    else :
        cnt = 1

small_cnt = 1
max_small_cnt = 1
# for i in range (N) :
    # if i == N-1 :
    #     if arr[i] <= arr[i - 1] :
    #         small_cnt += 1
    #         if max_small_cnt < small_cnt:
    #             max_small_cnt = small_cnt
    #     else :
#         small_cnt = 1

for i in range (N) :
    if i == N-1 :
        # if arr[i] <= arr[i - 1] :
        #     small_cnt += 1
        #     if max_small_cnt < small_cnt:
        #         max_small_cnt = small_cnt
        # else :
        #     small_cnt = 1
        break
    elif arr[i] >= arr [i + 1] :
        small_cnt += 1
        #print('arr[i] :',arr[i], 'i :', i, 'arr[i+1]', arr[i+1], 'small_Cnt :', small_cnt)
        if max_small_cnt < small_cnt :
            max_small_cnt = small_cnt
    else :
        small_cnt = 1

# print(max_small_cnt)
print(max(max_cnt,max_small_cnt))

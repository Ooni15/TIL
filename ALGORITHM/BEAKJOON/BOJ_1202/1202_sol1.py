N, K = map(int,input().split()) # N : 보석개수 K : 가방 개수
arr = [list(map(int,input().split())) for _ in range(N)]
C_arr = [0] * K
for i in range(K) :
    C_arr[i] = int(input())


# 가방 비싼 보석 순으로 정렬
arr.sort(key=lambda x:(-x[1],x[0]))
# 가방 작은 애부터
C_arr.sort()
max_value = 0
max_value_2 = 0
used_bags = [False] * K
used_jewel = [False] * N
# print(arr)
# print(C_arr)

# for weight, price in arr:
#     for j in range(K):
#         if not used_bags[j] and weight <= C_arr[j] :
#             max_value += price
#             used_bags[j] = True
#             break

for C in C_arr:
    for j in range(N):
        weight, price = arr[j][0], arr[j][1]
        if not used_jewel[j] and  weight <= C :
            max_value_2 += price
            used_jewel[j] = True
            break

print(max_value_2)


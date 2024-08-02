# arr1 = [0] *3
# arr2 = [[0] * 3 for _ in range(2)]

# for i in range(2) :
#     print(*arr2[i])
# for i in range(2) :
#     for j in range(3):
#         print(arr2[i][j], end = ' ')
#     print()

arr = [[1,2,3],[4,5,6]]

for i in range(n) :
    for j in range(m) :
        (arr[i][j + (m-1-2*j)*(i%2)])
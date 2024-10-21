K = int(input())
arr = [int(input()) for _ in range(K)]
max_weight = min(arr)

# 뒤에서부터 치는건?
arr.sort()

for i in range(K):
    weight = arr[i]*(K -i)
    if max_weight <= weight:
        max_weight = weight

print(max_weight)
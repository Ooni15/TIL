N = int(input())
max_length = 0
max_arr = []

for i in range(1, N + 1):
    arr = [N, i]  # 초기 수열을 설정
    length = 2

    while True:
        next_value = arr[-2] - arr[-1]
        if next_value < 0:
            break
        arr.append(next_value)
        length += 1

    if length > max_length:
        max_length = length
        max_arr = arr[:]

print(max_length)
print(*max_arr)

T = int(input())

for test_case in range(T) :
    arr = list(input())

    N = len(arr)
    # dir 인덱스가  0, 2면 y축 이동, 1,3이면 x축 이동
    # 뒤로 가면 -1 곱해주면 되는굥
    dir_F = [1, 1, -1, -1]
    dir_idx = 0
    x, y = 0, 0
    x_arr, y_arr = [0], [0]
    for i in range(N):

        if arr[i] == 'F':
            if dir_idx % 2 == 0:
                y += dir_F[dir_idx]
                y_arr.append(y)
            else:
                x += dir_F[dir_idx]
                x_arr.append(x)
        elif arr[i] == 'B':
            if dir_idx % 2 == 0:
                y -= dir_F[dir_idx]
                y_arr.append(y)
            else:
                x -= dir_F[dir_idx]
                x_arr.append(x)
        elif arr[i] == 'L':
            dir_idx = (dir_idx - 1 + 4) % 4
        elif arr[i] == 'R':
            dir_idx = (dir_idx + 1) % 4

    x_min, x_max, y_min, y_max = min(x_arr), max(x_arr), min(y_arr), max(y_arr)
    ans = (x_max - x_min) * (y_max - y_min)
    print(ans)



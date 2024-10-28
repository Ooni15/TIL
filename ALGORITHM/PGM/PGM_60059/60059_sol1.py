# 자물쇠 돌리는 거임
def rotation_90(arr):
    # 정사각형 버프
    n = len(arr)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = arr[i][j]

    return result


def check(new_lock_arr):
    N = len(new_lock_arr)
    real_N = N // 3
    for i in range(real_N, real_N * 2):
        for j in range(real_N, real_N * 2):
            if new_lock_arr[i][j] != 1:
                return False
    return True


def solution(key, lock):
    M = len(key)  # key 길이
    N = len(lock)  # lock 길이
    print(N)

    new_lock = [[0] * (3 * N) for _ in range(3 * N)]
    for i in range(N):
        for j in range(N):
            new_lock[i + N][j + N] = lock[i][j]

    # 4 방향으로 회전할 때,
    for m in range(4):
        key = rotation_90(key)
        for x in range(2 * N):
            for y in range(2 * N):
                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] -= key[i][j]

    return False

    # print(new_lock)
    # answer = True
    # return answer




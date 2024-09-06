def factorial (n) :
    return n * factorial(n-1) if n > 1 else 1

def count_case (x) :
    pass


# main
T = int(input())

for test_case in range (1, T + 1) :
    N = int(input())
    arr = list(map(int,input().split()))
    total = 0

    visited = [False] * (N + 1)
    left = []  # 왼 무게
    right = []  # 우 무게

    count_case(0)


    print(f'#{test_case} {total}')


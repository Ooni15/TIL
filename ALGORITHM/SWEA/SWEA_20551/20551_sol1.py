T = int(input())

for test_case in range(1, T + 1) :
    A, B, C = map(int,input().split())

    # A < B < C 구조를 만들 수 없는 케이스를 처리
    if B < 2 or C < 3  :
        print(f'#{test_case} -1')
        continue

    eat = 0 # 먹은 사탕 개수
    # 설계 : B가 C 이상일 때, B = C - 1이라면 최소 개수
    if B >= C :
        eat += B - (C - 1)
        B = C - 1
    # 설계 : A가 B 이상일 때, A = B - 1이라면 최소 개수
    if A >= B :
        eat += A - (B - 1)
        A = B - 1

    print(f'#{test_case} {eat}')


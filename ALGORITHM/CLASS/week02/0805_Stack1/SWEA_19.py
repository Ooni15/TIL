T = int(input())

for test_case in range ( 1, 1+ T) :
    s = input()
    N = len(s)
    ans = 1
    for i in range(N // 2) :
        if s[i] != s[N - 1 - i] :
            ans = 0
            break

    print(f'#{test_case} {ans}')
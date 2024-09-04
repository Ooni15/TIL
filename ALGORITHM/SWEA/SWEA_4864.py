T = int(input())

for test_case in range(1, T+1) :

    lst1 = input()
    lst2 = input()

    if lst1 in lst2 :
        print(f'#{test_case} 1')

    else :
        print(f'#{test_case} 0')
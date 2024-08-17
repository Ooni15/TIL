def mirror (S) :
    if S == 'b' :
        return 'd'
    elif S == 'p':
        return 'q'
    elif S == 'd' :
        return 'b'
    elif S == 'q' :
        return 'p'


# main
T = int(input())

for test_case in range(1 , T +1 ):

    lst1 = list(map(str, input()))
    result = ''
    for i in range(1, len(lst1)+1) :
        result += mirror(lst1[-i])

    print(f'#{test_case} {result}')
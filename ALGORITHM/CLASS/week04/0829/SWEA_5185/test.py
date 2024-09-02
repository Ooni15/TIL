def find_num(lst):
    if lst == ['0', '0', '0', '1', '1', '0', '1']:
        return 0
    elif lst == ['0', '0', '1', '1', '0', '0', '1']:
        return 1
    elif lst == ['0', '0', '1', '0', '0', '1', '1']:
        return 2
    elif lst == ['0', '1', '1', '1', '1', '0', '1']:
        return 3
    elif lst == ['0', '1', '0', '0', '0', '1', '1']:
        return 4
    elif lst == ['0', '1', '1', '0', '0', '0', '1']:
        return 5
    elif lst == ['0', '1', '0', '1', '1', '1', '1']:
        return 6
    elif lst == ['0', '1', '1', '1', '0', '1', '1']:
        return 7
    elif lst == ['0', '1', '1', '0', '1', '1', '1']:
        return 8
    elif lst == ['0', '0', '0', '1', '0', '1', '1']:
        return 9

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num_lst = []
    print(arr)

    for i in arr:
        if len(str(i[0])) > 2:
            num_lst.append(i[0])
            break

    str_lst = list(str(num_lst[0]))
    i = len(str_lst)-1
    while str_lst[i] == '0':
        str_lst.pop()
        i -= 1
    remainder = 7 - (len(str_lst) % 7)
    new_lst = []
    for i in range(remainder):
        new_lst.append('0')
    result_lst = new_lst + str_lst

    code_num = []
    for i in range(0, len(result_lst), 7):
        code_num.append(find_num(result_lst[i:i+7]))

    cal_num = (code_num[1]+code_num[3]+code_num[5]+code_num[7]) + (code_num[0]+code_num[2]+code_num[4]+code_num[6])*3

    if cal_num % 10 == 0:
        print(f'#{tc} {sum(code_num)}')
    else:
        print(f'#{tc} 0')
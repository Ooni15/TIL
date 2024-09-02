def hexadecimal_to_binary(n, hex_n) :
    binary_number = ""

    for i in range (n-1, -1 , -1) :
        cnt = 0
        check = 0

        if hex_n[i] == 'A' :
            num = 10
        elif hex_n[i] == 'B' :
            num = 11
        elif hex_n[i] == 'C' :
            num = 12
        elif hex_n[i] == 'D' :
            num = 13
        elif hex_n[i] == 'E' :
            num = 14
        elif hex_n[i] == 'F' :
            num = 15
        else :
            num= int(hex_n[i])


        while check == 0 :
            if num > 0 :
                remainder = num % 2
                binary_number = str(remainder) + binary_number
                num = num // 2
                cnt += 1
            elif num <= 0 & cnt != 4 :
                binary_number = "0" + binary_number
                cnt += 1

            if cnt == 4 :
                check += 1


    return binary_number

# main
T = int(input())

for test_case in range(1, T + 1) :
    str_N, hex_num = map(str, input().split())
    N = int(str_N)

    print(f'#{test_case}', hexadecimal_to_binary(N, hex_num))



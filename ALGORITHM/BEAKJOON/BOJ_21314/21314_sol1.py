number = input()
N = len(number)
M_cnt = 0
max_num = []
min_num = []

for i in range(N):
    if i == N-1 :
        if number[i] == 'M':
            M_cnt += 1
            num2 = '1' + '0' * (M_cnt - 1)
            num1 = '1' * M_cnt
            max_num.append(num1)
            min_num.append(num2)

    if number[i] == 'M':
        M_cnt += 1

    elif number[i] == 'K' :
        if M_cnt == 0 :
            num1, num2 = '5', '5'
        else :
            num1 = '1' + '0' * (M_cnt - 1) + '5'
            num2 = '5' + '0' * (M_cnt)

        M_cnt = 0

        max_num.append(num2)
        min_num.append(num1)



# print(max_num)
max_result = ''.join(max_num)
print(int(max_result))
min_result = ''.join(min_num)
print(int(min_result))
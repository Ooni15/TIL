# 남학생일 경우
def boy (personal_num, now) :
    M = len(now)
    for i in range (1, M) :
        if personal_num*i < M :
            if now[personal_num * i] == 0 :
                now[personal_num * i] = 1
            elif now[personal_num * i] == 1 :
                now[personal_num * i] = 0
    #print(now)
    return now


def girl (personal_num, now) :
    M = len(now)
    cnt = 0
    for i in range(1, M) :

        if personal_num - i > 0 and personal_num + i < M  :
            #print(personal_num - i, personal_num + i)
            if now[personal_num - i] != now[personal_num + i] :
                break
            elif now[personal_num - i] == now[personal_num + i] :
                cnt += 1
                if now[personal_num - i] == 0 :
                    now[personal_num - i] , now[personal_num + i] = 1, 1
                elif now[personal_num - i] == 1 :
                    now[personal_num - i], now[personal_num + i] = 0, 0

    if now[personal_num] == 0:
        now[personal_num] = 1
    elif now[personal_num] == 1:
    #print(now[personal_num])
        now[personal_num] = 0
    #print(now[personal_num])


    return now

# main
N = int(input())
switch = [0] +list(map(int,input().split()))
number = int(input())

for i in range(number) :
    sex, num = map(int, input().split())
    if sex == 1 :
        switch = boy(num, switch)
    else :
        switch = girl(num, switch)
        # print('여자지롱')


#print(len(switch))
for i in range(1, len(switch)):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()  # 20번째 숫자마다 줄바꿈

'''
8
0 1 0 1 0 0 0 1
2
1 3
2 1
'''
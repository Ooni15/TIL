T = int(input())

for testcase in range(1, T + 1):
    n = int(input())
    max_r = 0
    num = 1
    all = 0
    cnt = 0
    for i in range(1, n + 1):
        now = int(input())

        all += now
        if max_r <= now :
            if max_r == now:
                cnt += 1
            else:
                cnt = 0
            max_r = now
            num = i


    if cnt >=1:
        print('no winner')
    elif max_r > all // 2:
        print('majority winner', num)
    else :
        print('minority winner', num)

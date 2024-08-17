N = int(input())
switch = list(map(int, input().split()))
M = int(input())
student = [list(map(int, input().split()))for _ in range(M)]
# print(switch)
# print(student)

for x in student:
    if x[0] == 1:
        # len(switch)보다 작은 x[1]의 배수
        for i in range(1, len(switch)):
            if x[1] * i <= len(switch):
                switch[x[1] * i - 1] = int(not switch[x[1] * i - 1])
    else:               # 여자
        # x-1인덱스 쁠마로 같은지 비교 쁠마가 인덱스 초과 x
        switch[x[1] - 1] = int(not switch[x[1] - 1])
        for i in range(1, len(switch)):
            if x[1]+i <= len(switch) + 1 and x[1] - i >= 0:
                if switch[x[1] + i - 1] == switch[x[1] - i - 1]:
                    switch[x[1] + i - 1] = int(not switch[x[1] + i - 1])
                    switch[x[1] - i - 1] = int(not switch[x[1] - i - 1])
                else:
                    break
    # print(switch)

i = 0
while i <= N//20:
    print(*switch[20 * i: 20 * i + 20])
    i += 1


# 출력은 한줄에 20개씩
# 출력 때 int로 한번에 바꿀걸...
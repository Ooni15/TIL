N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

len_all = 0
i = 0
start = lst[0][0]
end = lst[0][1]

while True:
    j = i + 1

    # 막타면?
    if i == N - 1:
        len_all += (end - start)
        break

    next_x = lst[j][0]
    next_y = lst[j][1]

    if start <= next_x <= end :
        if end <= next_y:
            end = next_y
        i += 1

    else:
        len_all += (end - start)
        i += 1
        start = lst[i][0]
        end = lst[i][1]


print(len_all)
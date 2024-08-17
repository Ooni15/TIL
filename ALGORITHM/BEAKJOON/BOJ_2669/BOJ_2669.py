def make_arr (X1, Y1, X2, Y2) :

    arr = []
    for i in range(Y1, Y2) :
        for j in range(X1, X2) :
           arr.append([j, i])

    return arr


# main

total_arr = []
for i in range (4) :
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1, y2) :
        for j in range(x1, x2) :
           total_arr.append((j, i))

print(len(set(total_arr)))



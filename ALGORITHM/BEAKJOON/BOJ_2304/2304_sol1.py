N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

arr.sort()
cnt = 0
max_height = arr[N-1][1]
max_a = N-1
total = 0
Max_height = arr[0][1]
for i in range(len(arr)) :
    if Max_height < arr[i][1] :
        Max_height = arr[i][1]

print(Max_height)

for i in range (len(arr) - 1 , 0, -1) :
    if arr[i][1] > max_height :
        distance = arr[i][0] - arr[max_a][0]
        total += distance * max_height
        max_height = arr[i][1]
        if max_height == Max_height :


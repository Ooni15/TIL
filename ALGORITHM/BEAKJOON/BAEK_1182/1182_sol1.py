N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt_S = 0

for i in range (N) :
    for j in range (i+1, N+1) :
        find_S = 0
        find_S = sum(arr[i : j])
        if find_S == S :
            cnt_S += 1

print(cnt_S)
## 시간 초과난 코드

N , K = map(int,input().split())
arr = list(map(int,input().split()))

max_value = min(arr)

for i in range(N):
    if i + K - 1 < N :
        value = sum(arr[i: i + K ])
        if max_value < value :
            max_value = value

print(max_value)

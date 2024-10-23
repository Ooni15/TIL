N = int(input())
arr = list(map(int,input().split()))

dp = [1] * N

for i in range(1,N):
    for j in range(i):
        if arr[j] > arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1


print(N - max(dp))
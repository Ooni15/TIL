# 되겠냐
# 순서 반영이 안됨
N, K = map(int,input().split())
dp = [100000000] * 100001
cnt = [0] * 100001

dp[N] = 0
cnt[N] = 1

for i in range(N, K + 1):
    # 들어가는 거 한칸 전, 후 , 2x칸
    # 근데 0, 100000 이상이면 넣지마
    if i + 1 <= 100000:
        if dp[i + 1] > dp[i] + 1:
            dp[i+1] = dp[i] + 1
            cnt[i+1] = cnt[i]
        elif dp[i + 1] == dp[i] + 1:
            cnt[i+1] += cnt[i]
    if 0 <= i -1 :
        if dp[i - 1] > dp[i] + 1:
            dp[i - 1] = dp[i] + 1
            cnt[i - 1] = cnt[i]
        elif dp[i -1] == dp[i] + 1:
            cnt[i+1] += cnt[i]

    if 2 * i <= 100000:
        if dp[2 * i] > dp[i] + 1:
            dp[2*i] = dp[i] +  1
            cnt[2*i] = cnt[i]
        elif dp[2 * i] == dp[i] + 1:
            cnt[2*i] += cnt[i]



print(dp[5:34])
print(cnt[5:34])
print(dp[K])
print(cnt[K])


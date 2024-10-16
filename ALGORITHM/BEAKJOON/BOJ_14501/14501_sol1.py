N = int(input())

T = [0] * (N+1)
P = [0] * (N+1)
for i in range(1,N+1) :
    T[i], P[i] = map(int,input().split())

d = [0] * (21)

for i in range(1, N+1) :
    work = T[i]
    if i + work <= N + 1:
        max_price = max(d[:i])
        d[i + work] = max(d[i + work],d[i] + P[i], max_price + P[i])


print(max(d))

N, K = map(int,input().split())
cat = list(map(int,input().split()))

cat_s = sorted(cat)
cnt = 0

j = N -1

for i in range(N):

    while True:

        if j <= i :
            break

        if cat_s[i] + cat_s[j] <= K:
            cnt += 1
            j -= 1
            break
        else :
            j -= 1

print(cnt)
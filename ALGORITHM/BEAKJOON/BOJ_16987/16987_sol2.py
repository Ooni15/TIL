# 계란냠냠
def egg(now_egg, broken_egg, s, w):     # 현재 계란 친구. 깨진 계란 개수, 배열들

    global max_broken_egg


    if now_egg == N:
        # print(now_egg, broken_egg, s, w)
        if max_broken_egg <= broken_egg:
            max_broken_egg = broken_egg

        return

    if s[now_egg] <=0:
        egg(now_egg + 1, broken_egg, s, w)
        return

    can_hit = False

    for i in range(N):

        if i == now_egg or s[i] <=0 :
            continue

        can_hit = True

        original_now = s[now_egg]
        original_next = s[i]
        # 계란 후려치기
        s[i] -= w[now_egg]
        s[now_egg] -= w[i]

        # 2개 다 터져
        new_broken = broken_egg
        if s[now_egg] <=0:
            new_broken += 1
        if s[i] <= 0 :
            new_broken += 1

        egg(now_egg + 1, new_broken, s, w)


        s[now_egg] = original_now
        s[i] = original_next

        # 시벌탱 이거다
    if not can_hit:
        egg(now_egg + 1, broken_egg, s, w)

# main
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
S = [0] * N
W = [0] * N
broken_egg = [0] * N
max_broken_egg = 0
for i in range(N):
    S[i] = arr[i][0]
    W[i] = arr[i][1]

egg(0, 0, S, W)

print(max_broken_egg)
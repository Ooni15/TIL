# 계란냠냠
# 빡대가리 이슈
def egg():

    for i in range(N):
        next_index = i
        if i == N-1:
            break
        if broken_egg[i] == 0:
            while True:
                next_index += 1
                # 나보다 오른쪽에 계란 없으면 return
                if next_index >= N:
                    break
                # 지금 내가 받은 계란으로 옆에꺼 쳐 때리기
                S[i] -= W[next_index]
                S[next_index] -= W[i]
                print(i, S[i], S[next_index])

                if S[next_index] <= 0:
                    broken_egg[next_index] = 1

                if S[i] <= 0 :
                    broken_egg[i] = 1
                    break


# main
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
S = [0] * N
W = [0] * N
broken_egg = [0] * N
for i in range(N):
    S[i] = arr[i][0]
    W[i] = arr[i][1]

egg()

print(broken_egg)
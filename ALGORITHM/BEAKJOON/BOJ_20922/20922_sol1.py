from collections import deque

N, K = map(int,input().split())  # 총 길이, K개 이하 포함
arr = list(map(int,input().split()))
max_num = max(arr)
a = [0] * (max_num + 1)
# a = [0] * 100001    # count 배열

queue = deque()
len = 0
final = []

for i in range(N):
    a[arr[i]]  += 1


    if a[arr[i]] == K + 1:
        final.append(len)
        while queue:
            info = queue.popleft()
            check, idx = info[0], info[1]
            a[check] -= 1
            len -= 1
            if check == arr[i]:
                break

    len += 1
    if i == N-1:
        final.append(len)
        break
    queue.append([arr[i], i])
    # queue.append([arr[i],i])



print(max(final))


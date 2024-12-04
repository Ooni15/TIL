N = int(input())
A = list(map(int,input().split()))
count_arr = [1] * (N)

for i in range(1,N):
    for j in range(i):
        if A[i] > A[j] and count_arr[i] < count_arr[j] + 1:
            count_arr[i] = count_arr[j] + 1
# print(count_arr)

max_len = max(count_arr)
final = []
current_len = max_len
current_value = 1000
for i in range(N - 1, -1, -1):
    if count_arr[i] == current_len:
        final.append(A[i])
        current_value = A[i]
        current_len -= 1
    if current_len == 0 :
        break

# 결과 출력
final.reverse()  # 역순으로 추가했으므로 뒤집기
print(max_len)
print(*final)
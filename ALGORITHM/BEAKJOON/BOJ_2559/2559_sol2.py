N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 처음 K개의 요소의 합을 초기 최대값으로 설정
current_sum = sum(arr[:K])
max_value = current_sum

# 슬라이딩 윈도우를 사용하여 연속된 K개의 합을 갱신
for i in range(K, N):
    current_sum += arr[i] - arr[i - K]      # 한놈은 더해주고 한놈은 빼주고
    if current_sum > max_value:
        max_value = current_sum

print(max_value)

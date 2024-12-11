N = int(input())
arr = [0] + list(map(int,input().split()))
stack = []
result = [0] * (N + 1)

for i in range(1, N + 1):
    while True:
        if not stack:
            result[i] = 0
            stack.append([arr[i], i])
            break

        if stack[-1][0] >= arr[i]:
            result[i] = stack[-1][1]
            stack.append([arr[i],i])
            break
        else:
            # 나보다 작으면 다 쳐내
            stack.pop()

print(*result[1:])



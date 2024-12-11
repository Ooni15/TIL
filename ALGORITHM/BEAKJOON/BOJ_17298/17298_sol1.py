N = int(input())
arr = list(map(int,input().split()))

stack = []
result = [0] * N

for i in range(N - 1,-1,-1):

    while True:

        if not stack:
            result[i] = -1
            stack.append(arr[i])
            break

        if stack[-1] > arr[i]:
            result[i] = stack[-1]
            stack.append(arr[i])
            break
        else:
            stack.pop()

print(*result)
n = int(input())

arr = [0] * n
for i in range(n):
    arr[i] = int(input())

stack = []
result = []

now = 0
i = 0
while True:

    if i >= n:
        for j in range(len(result)):
            print(result[j])
        break

    if now < arr[i]:
        now += 1
        stack.append(now)
        result.append('+')

    elif stack and arr[i] == stack[-1]:
        stack.pop()
        i += 1
        result.append('-')

    else:
        print("NO")
        break


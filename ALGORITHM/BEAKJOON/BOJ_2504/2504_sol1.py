message = input()
M = len(message)
stack = []
temp = 1
ans = 0
for i in range(M):

    if message[i] == '(':
        stack.append(message[i])
        temp *= 2
    elif message[i] == '[':
        stack.append(message[i])
        temp *= 3
    elif message[i] == ')':
        if not stack or stack[-1] != '(':
            ans = 0
            break
        elif message[i - 1] == '(':
            ans += temp
        stack.pop()
        temp //= 2
    elif message[i] == ']':
        if not stack or stack[-1] != '[':
            ans = 0
            break
        elif message[i - 1] == '[':
            ans += temp
        stack.pop()
        temp //= 3

if stack :
    ans = 0

print(ans)
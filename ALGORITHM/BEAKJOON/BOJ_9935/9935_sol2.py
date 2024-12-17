letters = input()
bomb = list(input())

stack = []

N = len(letters)
bomb_len = len(bomb)

for i in range(N):
    stack.append(letters[i])
    if stack[-1] == bomb[-1]:
        if stack[-bomb_len:] == bomb:
            for j in range(bomb_len):
                stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))


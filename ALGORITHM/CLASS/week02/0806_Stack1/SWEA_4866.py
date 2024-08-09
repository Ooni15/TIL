T = int(input())

for test_case in range (1, 1 + T) :

    arr = list(map(str,input()))

    stack_size = len(arr)
    stack = [0] * stack_size
    top = -1
    result = -1

    for i in range(stack_size) :

        if arr[i] == '(' :
            top += 1
            stack[top] = 1
            #print('(', i, stack)
        elif arr[i] == '{' :
            top += 1
            stack[top] = 2
            #print('{', i, stack)
        elif arr[i] == ')' :
            top -= 1
            if top < -1 :
                result = 0
                break
            elif stack[top + 1] == 1 :
                result = 1
            else :
                result = 0
                break
        elif arr[i] == '}' :
            top -= 1
            if top < -1 :
                result = 0
                break
            elif stack[top + 1]  == 2 :
                result = 1
            else :
                result = 0
                break
    #print(top)
    if top > -1 :
        result = 0

    print(f'#{test_case} {result}')

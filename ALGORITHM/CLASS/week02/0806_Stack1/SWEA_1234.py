T = 1

for test_case in range(1, T + 1) :
    N, arr = input().split()
    N = int(N)
    stack = []
    i = 0

    while 0 <= i <= N :
        if i == 0 :
            stack.append(arr[i])
            print(stack)
            i += 1
            print(i)
        else  :
            if arr[i] == arr[i + 1] :

                stack.pop()
                i += 2
                print(i)
            else :
                stack.append(arr[i])
                i += 1
                print(i)
                print(stack)

    print(arr)


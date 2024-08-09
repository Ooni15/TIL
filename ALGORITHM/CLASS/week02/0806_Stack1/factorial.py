def fact(n) :
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(5))

def f(n) :
    global cnt
    cnt += 1
    if n == 1:
        return
    else :
        f(n-1)

cnt = 0
f(100)
print(cnt)

def f2(i, N ) :      # i 현재 인덱스, N 크기
    global arr
    if i == N :
        return
    else :
        print(arr[i])
        f2(i+1, N)
        return      # 함수 끝에 return 없어도 알아서 끝날 줄 알아

arr = [1, 2, 3, 4]
print(f2(0, 4))
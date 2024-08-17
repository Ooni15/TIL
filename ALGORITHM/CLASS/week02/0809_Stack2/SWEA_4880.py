dct_win = {
    1 : 3,
    2 : 1,
    3 : 2
}

def win (k, t) :

    a = arr[k]
    b = arr[t]
    #print(k, t)
    if a == b :
        return k
    else :
        if dct_win[a] == b :
            #print('k:', k,'a:', a,'t:', t,'b:', b)
            return k
        else :
            #print('k:', k, 'a:', a, 't:', t, 'b:', b)
            #print(b)
            return t

# 나누는 아이
def f(i,j) :
    if i == j:
        return i
    else :  # 두명 이상이면 나눠
        left = f(i, (i+j)//2)       # 왼쪽 그룹
        right =f((i + j)//2 + 1, j)  # 오른쪽 그룹
        return win(left, right)     # 두 그룹의 승자를 찾는 함수


# main
T = int(input())

for test_case in range(1, T + 1) :

    N = int(input())
    arr = [0] + list(map(int,input().split()))
    winner = f(1,N)
    print(f'#{test_case} {winner}')

    """
1
4
1 3 2 1
    """

    """
1    
7
1 3 3 3 1 1 3
    """
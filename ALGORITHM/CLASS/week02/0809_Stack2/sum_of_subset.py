def f(i, K) :   #bit[i]를 결정하는 함수
    if i == K : # 모든 원소에 대해 결정하면
        s= 0
        for j in range(K) :
            if bit[j] :     # bit[j]가 0이 아니면
                print(a[j], end = ' ')
                s += a[j]
        print(' : ', s)         # 부분집합을 한 행에 표시
    else :
        # bit[i] = 1
        # f(i + 1, K)
        # bit[i] = 0
        # f(i + 1, K)
        for j in [1, 0] :
            bit[i] = j
            f(i + 1, K)


N = 3
a = [1, 2, 3]   # 주어진 원소의 집합
bit = [0] * N   # 원소의 포함여부를 표시하는 배열


f(0, N)     # 0번 인덱스 부터 N개야/ N개의 원소에 대해 부분집합을 만드는 함수




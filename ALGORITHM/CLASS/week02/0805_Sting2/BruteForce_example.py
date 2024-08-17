def f(t,p) :        # 패턴 p와 일치하는 구간의 시작인덱스 리턴,
    M = len(t)
    N = len(p)

    for i in range(M - M + 1) : # 비교 시작 위치
        for j in range(M) :
            if t[i + j] != p[j]:
                break
        else :  # for j, 다음 글자부터 비교 시작
            return i        # 패턴을 찾은 경우
    return -1


p = 'TTA'
t = 'TTTTTATTATTTTA'

print(f(t,p))
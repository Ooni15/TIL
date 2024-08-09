p = 'is'    # 찾을 패턴
t = 'This is a book~!'  # 전체 텍스트
M = len(p)  # 찾을 패턴의 길이
M = len(t)  # 전체 텍스트의 길이

def BruteForce(p,t) :
    i = 0
    j = 0
    while j < M and i < N :
        if t[i] != p[j] :
            i = i -j
            j = -1
        i = i + 1
        j = j + 1
    if j == M :
        return i - M
    else :
        return -1

p = 'TTA'
t = 'TTTTTATTATTTTA'

N = len(t)
M = len(p)
cnt = 0
for i in range(N - M + 1) :     # 비교 시작 위치
    for j in range(M) :
        if t[i + j] != p[j] :
            break       # for j, 다음 글자부터 비교 시작
    else :      # for j가 중단없이 반복되면
        cnt += 1    # 패턴 개수 1 증가

print(cnt)


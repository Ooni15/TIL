# 횟수를 바로 다이나믹 테이블에 넣기
X = int(input())

d = [0] * 10000001

for i in range(2, X+1) :
    # 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 2로 나눠지는 경우
    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2] + 1)
    # 3로 나눠지는 경우
    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3] + 1)


print(d[X])

num = 45678
c= [o]
i = 0
tri = run = 0
while i < 10 :
    if c[i] >=3 : #triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue

    if c[i]
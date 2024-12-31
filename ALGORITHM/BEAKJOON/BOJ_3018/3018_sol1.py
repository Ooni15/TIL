# 쓰레기 문제
N = int(input())
# 선영이 1번
E = int(input())
party_total = []
party_people = []
for i in range(E):
    lst = list(map(int,input().split()))
    total = lst[0]
    people = lst[1:]
    people.sort()

    # 1번이랑 논 날 부터 시작이네


    party_total.append(lst[0])
    party_people.append(lst[1:])


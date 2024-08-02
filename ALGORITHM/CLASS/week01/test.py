
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bs = [0] * 5001  # 5000번까지의 버스 정류장 리스트

    for i in range(N):  # N개의 버스가 지나갈 때
        a, b = map(int, input().split())  # 버스의 시작 정류장부터 끝 정류장을 변수 a, b에 할당
        for bus in range(a, b + 1):  # a부터 b까지의 버스 정류장을 지나가는 것을
            bs[bus] += 1  # bs 리스트에 카운트 정렬로 할당.

    P = int(input())
    stops = [0] * P  # 버스가 지나는 개수를 알고 싶은 버스 정류장의 번호 개수만큼 빈 리스트 할당
    ls = []  # stops에서 지나가는 버스 정류장에 지나가는 버스의 개수를 위한 빈 리스트
    for i in range(P):
        stops[i] = int(input())  # 버스 정류장의 번호 리스트에 더하기

    for stop in stops:  # 버스 정류장의 번호를 불러와서
        ls.append(bs[stop])

    print(f'#{tc}', *ls)
# 시작점 : 0번 점원 ? 탑의 높이는 0부터 시작
# 끝점(기저조건) : N명의 점원을 탑에 쌓을지 말지 고려를 완료

# 명시된 조건 : 모든 점원을 쌓았는데, B 이하인 경우를 고려하지 않음
# - 문제 조건에 이게 없으면 B 이하인 ans도 따로 만들어주어야 한다.

import sys
sys.stdin = open('input.txt', 'r')

def recur (cnt, sum_height) :
    global ans

    # 기저 조건 가지치기. 이미 탑의 높이가 B 이상이라면, 더 이상 확인할 필요 X
    if sum_height >= B:
        ans = min(ans, sum_height)
        return

    # 기저조건. 모든 점원을 탑을 쌓는데 고려했는가 ?
    if cnt == N :
        return


    # cnt 번 점원을 탑에 쌓는다
    recur(cnt + 1, sum_height + heights[cnt])
    # 안쌓는다
    recur(cnt + 1, sum_height)

    # 안쌓는다다
T = int(input())

for test_case in range(1, T + 1) :
    N, B = map(int,input().split())
    heights = list(map(int,input().split()))    # 각 점원의 키
    ans = 1e9   # 점원들을 쌓은 탑 중 B에 가장 가까운 높이를 저장, 1억!
    recur(0, 0)
    print(f'#{test_case} {ans - B}')

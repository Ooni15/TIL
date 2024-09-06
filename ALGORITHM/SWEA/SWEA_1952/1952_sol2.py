# 접근 방법 2
# 3월 기준으로 생각 : 2월까지의 최소 금액 + 본인의 금액 중 최소금액
# 이전의 최소 금액들을 활용해서 내 최소 금액을 구할 수 있다!
# DP 활용하기
# 왜 DP로 활용 가능한가?
# 1. 작은 문제로 분할 가능해야한다.
#   - 전체 문제의 합 = 각 달까지의 최소 금액들이 쌓여서 완성
#   - 각 달까지의 최소 금액 문제로 생각
# 2. 뒤에 결과를 구할 때, 앞에서 구했던 결과가 변하면 안된다.

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for test_case in range(1, T + 1) :
    cost = list(map(int, input().split()))
    # 인덱스 헷갈림 방지 -> 0 만들기
    days = [0] + list(map(int, input().split()))
    dp = [0] * 13   # 1-12월 최소 금액들을 저장

    for i in range(1, 13) :
        # 현재 달의 최소 비용을 계산
        # 1-2월 까지는 이전 달 + 1일권 구입 / 이전 달 + 1달 권
        # 이전 달 + 1일 권 구입 / 이전 달  + 1달 권/ 3달 전에 3달 권 구입 중 최소
        dp[i] = min(dp[i-1] + (days[i] * cost[0]), dp[i-1] + cost[1])

        # 인덱스 오류를 피하기 위해 3월 이후 계산을 따로 작성
        if i >= 3 :
            dp[i] = min(dp[i], dp[i - 3] + cost[2])

    # 12월 까지의 계산 결과 vs 1년권
    result = min(dp[12], cost[3])

    print(f'#{test_case} {result}')
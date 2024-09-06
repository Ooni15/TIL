import sys
sys.stdin = open('input.txt', 'r')

# 시작점 : 1월 / 누적 금액 : 0 원
# 끝점 : 12월
def dfs (month, sum_cost) :
    global ans
    # 기저 조건. 12월까지 모두 보았는가?
    if month > 12 :
        ans = min(ans, sum_cost)
        return


    # 1일권으로 모두 구매 (다음 재귀 : 다음 달을 확인)
    dfs(month + 1, sum_cost + (days[month] * cost[0]))
    # 1달권 구매    (다음 재귀 : 다음 달을 확인)
    dfs(month + 1, sum_cost + cost[1])
    # 3달권 구매    (다음 재귀 : 3달 후를 확인)
    dfs(month + 3, sum_cost + cost[2])
    # 1년권 구매    (다음 재귀 : 12달 후를 확인)
    dfs(month + 12, sum_cost + cost[3])
    # - 사실 1년권은 재귀에서 빼고, 1월에 구입한 비용이랑 비교해도 된다
    # - 직관적으로 보기 위해 강의용으로 추가

T = int(input())

for test_case in range(1, T + 1) :
    cost = list(map(int, input().split()))
    # 인덱스 헷갈림 방지 -> 0 만들기
    days = [0] + list(map(int, input().split()))
    ans = 1e9       # 최대값 넣어줘
    dfs(1, 0)
    print(f'#{test_case} {ans}')


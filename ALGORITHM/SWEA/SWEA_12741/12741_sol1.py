# 시간 초과 날 거임
#채점용 input 파일로 채점한 결과 fail 입니다.
#(오답 : 50000개의 테스트케이스 중 32355개가 맞았습니다.)
# 출력만 5만 번 -> 이걸 for문에서 돌리면 input과 ouput이 번갈아가면서 발생

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range (1, T + 1) :
    A, B, C, D = map(int, input().split())

    # 나중에 켜진 전구 시간의 시작점
    start = max(A, C)

    # 먼저 꺼진 전구의 시간이 끝점
    end = min(B, D)

    result = end - start
    if result <= 0 :
        result = 0

    print(f'#{test_case} {result}')


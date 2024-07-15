#import sys
#sys.stdin = open("ALGORITHM/Personal/SWEA/SWEA_1959/input (2).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N, M= map(int,input().split())
    list_A = list (map(int,input().split()))
    list_B = list (map(int,input().split()))

    max_sum=0
    if N < M :
        for i in range (M-N+1):
            sum = 0
            for j in range (N):
                sum += list_A[j]*list_B[j+i]
            if max_sum < sum : 
                max_sum = sum

    elif N > M :
        for i in range (N-M+1):
            sum = 0
            for j in range (M):
                sum += list_B[j]*list_A[j+i]
            if max_sum < sum : 
                max_sum = sum

    else : 
        for i in range (M) :
            sum += list_A[i]*list_B[i]
            max_sum = sum

    print(f'#{test_case} {max_sum}')
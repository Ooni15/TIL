# for i in range(1,4) :
#     for j  in range (1,4) :
#         print(i, end = '')
#         print(j)
#         # print(i, j)


# def KFC (x) :
#
#     x += 1
#     KFC(x)
#
# KFC(0)
# print('끝')

# # 순열만들기
# def Permitation(x) :
#
#
#     if x == 3 :
#         print(path)
#         return
#
#     for i in range(3) :
#         path.append(i)
#         Permitation(x+1)
#         path.pop()


path = []       # 경로를 기록할 리스트
used = [0] * 8  # 1-6까지 사용할 곳=
# Permitation(0)

# 기저 조건
def recur(level) :
    if level ==3 :
        print(*path)
        return
# 후보군을 반복함녀서
    for i in range(1,7) :
        # i가 이미 뽑혔다면, pass 해라
        # 아래 코드의 단점 : "in" = O(len(path))
        # 시간 초과 위험도가 높다!
        # if i in path :
        #     continue
        if used[i] == 1:
            continue
        # 2.1 재귀 호출 전 - 경로 기록 + 사용 기록
        used[i] = 1
        path.append(i)
        # 2.2 다음 재귀 호출 (파라미터 전달)
        recur(level + 1)
        # 2.3 돌아왔을 때 - 사용했던 경로 삭제
        path.pop()
        used[i] = 0

recur(0)
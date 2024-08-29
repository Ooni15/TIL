
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
# 전위 순회 (나 -> 왼쪽 -> 오른쪽)
def pre_order(node):
    if node == 0 :
        return

    print(node, end = ' ')      # 이거를 어디에 두냐에 따라 달라짐
    pre_order(left[node])
    # print(node, end=' ')      # 여기면 중위 순회
    pre_order(right[node])
    # print(node, end=' ')      # 여기면 후위

N = int(input())        # 1번부터 N번까지인 정점
E = N-1
arr = list(map(int, input().split()))
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장
# left [3] = 2 ==> 3번 부모의 왼쪽 자식은 2이다.
right = [0]*(N+1)       # 오른쪽 자식 번호를 저장할 리스트
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장

for i in range(E):
    parent, child = arr[i*2], arr[i*2+1]
# for i in range(0,E*2, 2):
#         p, c = arr[i], arr[i + 1]
    if left[parent]==0:          # 왼쪽자식이 없으면
        left[parent] = child
    else:
        right[parent] = child
    par[child] = parent

c = N
while par[c]!=0:        # 부모가 있으면
    c = par[c]          # 부모를 새로운 자식으로 두고
root = c                # 더이상 부모가 없으면 root
print(root)
pre_order(root)
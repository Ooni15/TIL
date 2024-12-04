#### 포기 #####
import itertools
from itertools import combinations
N, M = map(int,input().split())
arr = [[0]*(N+1)] + [[0] +list(map(int,input().split())) for _ in range(N)]

house = []
chi = []

for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 0:
            continue

        if arr[i][j] == 1:
            house.append([i,j])
        else:
            chi.append([i,j])


new_chi_lst= list(combinations(chi,1))
# print(new_chi_lst)

l_house = len(house)
# l_chi = len(new_chi_lst)

# final_len = [0] * l_chi
# for i in range(l_chi):
#     house_len = [0] * l_house
#     for j in range(l_house):
#         xc, yc = chi[i][0], chi[i][1]
#         xh, yh = house[j][0], house[j][1]
#
#         house_len[j] = abs(xc-xh) + abs(yc-yh)
#     print(house_len)
#     final_len[i] = min(house_len)

# for i in range(l_house):
#     chi_len = [0] * l_chi
#     for j in range(l_chi):
#         xc, yc = new_chi_lst[j][0], new_chi_lst[j][1]
#         xh, yh = house[i][0], house[i][1]
#         chi_len[j] = abs(xc - xh) + abs(yc - yh)
#     # print(chi_len)
#     final_len[i] = min(chi_len)

final_len = [0] * l_house
real_fin = []
for k in range(1, M+1):
    new_chi_lst = list(combinations(chi, k))
    # print(new_chi_lst)
    l_chi = len(new_chi_lst[0])
    for l in range(len(new_chi_lst)):

        for i in range(l_house):
            chi_len = [0] * l_chi
            for j in range(l_chi):
                xc, yc = new_chi_lst[l][j][0], new_chi_lst[l][j][1]
                xh, yh = house[i][0], house[i][1]
                chi_len[j] = abs(xc-xh) + abs(yc-yh)
            # print(chi_len)
            final_len[i] = min(chi_len)
        real_fin.append(sum(final_len))
print(min(real_fin))



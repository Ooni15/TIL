from itertools import combinations
# 뿌릴 수 있는 경우의 수를 겟챠 해보쟈~!~!~!~!~!
def comb(lst, G_size, R_size):
    all_combinations = []
    for Green in combinations(lst, G_size):
        remaining_elements = []
        for x in lst :
            if x not in Green:
                remaining_elements.append(x)
        for Red in combinations(remaining_elements, R_size):
            all_combinations.append([list(Green),list(Red)])
    return all_combinations



N, M, G, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 0 호수, 1 배양액 못뿌리는 땅, 2 배양액 뿌릴 수 있는 땅!
# 뿌릴 수 있는 땅 찾기
seed_ground = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            seed_ground.append((i,j))

# R, G 기본으로 뿌릴 곳 찾아보기
print(comb(seed_ground, G, R))
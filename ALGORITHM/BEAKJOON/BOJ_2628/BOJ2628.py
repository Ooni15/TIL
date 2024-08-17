N , M = map(int,input().split())
K = int(input())
N_lst = [0, N]
M_lst = [0, M]

for i in range (K) :
    a, b = map(int,input().split())
    if a == 0 :
        M_lst.append(b)
    else :
        N_lst.append(b)

N_lst.sort()
M_lst.sort()

# print(N_lst)
# print(M_lst)

diff_N_lst = [0] * (len(N_lst) - 1)
diff_M_lst = [0] * (len(M_lst) - 1)
# print(len(N_lst) - 1)
for i in range (len(N_lst) - 1) :
    diff_N_lst[i] = N_lst[i + 1] - N_lst[i]

for j in range (len(M_lst) - 1) :
    diff_M_lst[j] = M_lst[j + 1] - M_lst[j]

print(max(diff_N_lst) * max(diff_M_lst))



arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

def get_sub(tar) :
    cnt = 0     # 1의 개수를 count
    for i in range(n) :
        if tar & 0x1 :
            #print(arr[i], end = ' ')
            cnt += 1
        tar >>= 1
    return cnt

result = 0
for tar in range(0, 1 << n) :
    if get_sub(tar) == 3  :
        print()
print(result)

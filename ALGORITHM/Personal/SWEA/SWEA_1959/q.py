N=3
M=5
list_A=[1,5,3]
list_B=[3,6,-7,5,4]
a=list_A[1]*list_B[2]
print(a)
'''
for i in range (M-N+1):
        for j in range (M):
            sum += list_A[j]*list_B[j+i]
        if max_sum < sum : 
            max_sum = sum 
            '''
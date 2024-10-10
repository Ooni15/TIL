## 대실패!!!
N, K = map(int,input().split())
word = list(input() for _ in range (N))
word_set_lst = [0] * N
result = 0

if K < 5 :
    result = 0

else:
    teach = {'a','n','t','c','i'}   # set으로 만들기
    word.sort(key=len)      # 길이를 기준으로 sort
    for i in range(N) :
        word_set_lst[i] = set(word[i])

    first_set = word_set_lst[0] | teach

    if len(first_set) > K :
        result = 0

    else :
        for i in range(N):
            a = word_set_lst[i] | first_set
            if len(a) <= K :
                first_set = a
                result += 1

print(result)





        # a = word[i] + teach
        # print(a)














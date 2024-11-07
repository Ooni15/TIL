sentence = input()
bomb = input()

N = len(sentence) # 전체 문장의 길이
M = len(bomb)   # 폭파 문자열 길이
i = 0
while N-M-i >= 0 :
    if sentence[N-M-i] != bomb[0]:
        i += 1
    else :
        if sentence[N-M-i:N-i] == bomb:
            sentence = sentence[:N-M-i] + sentence[N-i:]
            # print(sentence)
            N = len(sentence)  # 전체 문장의 길이
            i -= (-1 + M)
            if N == 0 :
                sentence = 'FRULA'

print(sentence)
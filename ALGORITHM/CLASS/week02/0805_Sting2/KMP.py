target = "Hello SSAFY 12th!"  # target
pattern = "SSA"  # 우리가 찾을 패턴

def BruteForce(pat, text) :
    # 주로 먼저 돌릴 아가한테 N을 주는 편
    N = len(text)
    M = len(pat)
    i = 0   # text의 인덱스
    j = 0   # 패턴의 인덱스

    while j < M | i < N :     #  둘 중 하나만 만족해도 종료해도 돼

        # 틀린 곳을 발견했다면, index 값을 초기화 시킴.
        if text[i] != pattern[j] :
            # text의 현재 위치에서 일치하지 않는 곳을 발견!
            # 지금 위치 - j
            i = i - j # 현재 위치
            j -= 1  # 어차피 아래에서 1 더해줄거니까 -1로 해 / 원래면 0

        i = i + 1
        j = j + 1

        # 검색 성공
        if j == M :
            return i - M
        else :
            return -1

# 심플 버전
text = "This is simple version"
pattern = 'si'

def BruteForce2(pat, text) :

    for idx in range(len(text) - len(pat) + 1) :
        # 패턴을 처음부터 끝까지 순회
        for i in range(len(pattern)) :

            #1. 다르면, break
            if text[idx + j] != pat[j]:
                break
            # 같다면(다른게 없다면)
        else :
            return idx

    else :
        return -1
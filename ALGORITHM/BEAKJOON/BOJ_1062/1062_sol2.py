N, K = map(int, input().split())
words = [input().strip() for _ in range(N)]

essential_chars = {'a', 'n', 't', 'i', 'c'}

if K < 5 :
    print(0)

else :
    # 추가로 배울 수 있는 문자 개수
    additional_count = K - 5

    # 가능한 추가 문자의 후보 찾기
    unique_chars = set()
    for word in words:
        unique_chars.update(word[4:-4])

    # 필수 문자인 추가 문자 후보
    possible_chars = list(unique_chars - essential_chars)

    max_readable_words = 0

    # 비트마스크 사용하기
    total_possible = len(possible_chars)

    for mask in range(1 << total_possible):
        # 현재 조합의 문자를 저장
        learned_chars = set(essential_chars)

        for  i in range(total_possible):
            if mask & (1 << i) :
                learned_chars.add(possible_chars[i])
            if len(learned_chars) <= K :
                count = 0
                for word in words:
                    if all(c in learned_chars for c in word) :
                        count += 1
                max_readable_words = max(max_readable_words, count)

    print(max_readable_words)



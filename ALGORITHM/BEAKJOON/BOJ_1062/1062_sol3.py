from itertools import combinations

N, K = map(int, input().split())
words = [input().strip()[4:-4] for _ in range(N)]  # "anta"와 "tica"를 제거한 단어들

# 필수 문자
essential_chars = {'a', 'n', 't', 'i', 'c'}
if K < 5:
    print(0)
    exit()

# 여유 문자의 후보
possible_chars = set('abcdefghijklmnopqrstuvwxyz') - essential_chars
max_readable_words = 0

# 조합을 통한 탐색
for additional_chars in combinations(possible_chars, K - 5):
    learned_chars = essential_chars | set(additional_chars)
    count = 0
    for word in words:
        if all(c in learned_chars for c in word):
            count += 1
    max_readable_words = max(max_readable_words, count)

print(max_readable_words)
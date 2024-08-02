def count_binary_search(books, page) :      # 이진 탐색 횟수 계산 함수

    l = 1               # 책 시작 페이지
    r = books           # 책 끝 페이지
    cnt = 0

    while l <= r :
        center_page = int((l+r)/ 2)     # 이진 탐색을 위한 중간페이지
        if page == center_page :        # 페이지 찾으면 while문 끝
            break
        elif page > center_page :       # 찾고자 하는 페이지가 중간 페이지 보다 값이 크면 오른쪽 재탐색
            l = center_page
            cnt += 1                    # 이진탐색 횟수 카운트
        elif page < center_page :       # 찾고자 하는 페이지가 중간 페이지 보다 값이 작으면 왼쪽 재탐색
            r = center_page
            cnt += 1

    return cnt

def game(books, A, B) :     # 이진 탐색 게임 룰이 담긴 함수

    cnt_A = count_binary_search(books,A)    # A의 탐색 횟수
    cnt_B = count_binary_search(books,B)    # B의 탐색 횟수

    # A, B 탐색횟수 비교
    if cnt_A > cnt_B :
        return 'B'
    elif cnt_A < cnt_B :
        return 'A'
    else :
        return 0

# main
T = int(input())

for test_case in range(1, T + 1) :
    book, A, B = map(int,input().split())   # 입력값 받기
    print(f'#{test_case} {game(book, A , B)}')  # game 함수에 입력값 넣은 후 출력

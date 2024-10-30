# JavaScript_Ajax with Django

날짜: 2024년 10월 30일

## Ajax with follow

기존 

- HTML의 form 태그를 사용해 POST 메서드로 데이터를 제출(submit)

변경

- axios를 사용해 POST 메서드로 데이터 제출
- form의 method, action 속성이 불필요
- 팔로우 버튼에 submit 이벤트가 발생하면 (이벤트 리스너)
- django가 json 데이터를 응답
- JS에서 json 응답받은 json 데이터를 활용해 팔로우 버튼을 조작 (DOM)

## Ajax 적용

- form 요소 선택을 위해 id 속성 지정 및 선택
- action과 method 속성은 삭제
    - 요청은 axios로 대체되기 때문

### ‘data-*’ 속성

사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM사이에서 교환할 수 있는 방법

- 모든 사용자 지정 데이터는 JavaScript에서 datasest 속성을 통해 접근
- 주의사항
    1. 대소문자 여부에 상관없이 ‘xml’ 문자로 시작 불가
    2. 세미콜론 포함 불가
    3. 대문자 포함 불가

```jsx
# accounts/profile.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>{{ person.username }}의 프로필</h1>
  <div>
    팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span>
    / 팔로워 : <span id='followers-count'>{{ person.followers.all|length }}</span>
  </div>

  {% if request.user != person %}
    <div>
      <form id="follow-form" data-user-id="{{ person.pk }}">
        {% csrf_token %}
        {% if request.user in person.followers.all %}
        {% comment %} 12. class 지정해주기 {% endcomment %}
          <input type="submit" value="언팔로우" class='follow-input'>
        {% else %}
          <input type="submit" value="팔로우" class='follow-input'>
        {% endif %}
      </form>
    </div>
  {% endif %}

  {% comment %} 유저가 작성한 게시글 {% endcomment %}
  <h2>{{ person.username }} 작성한 게시글</h2>
  {% for article in person.article_set.all %}
    <p>{{ article }}</p>
  {% endfor %}

  <hr>

  {% comment %} 유저가 작성한 댓글 {% endcomment %}
  <h2>{{ person.username }} 작성한 댓글</h2>
  {% for comment in person.comment_set.all %}
    <p>{{ comment }}</p>
  {% endfor %}

  <hr>

  {% comment %} 유저가 좋아요한 게시글 {% endcomment %}
  <h2>{{ person.username }} 좋아요한 게시글</h2>
  {% for article in person.like_articles.all %}
    <p>{{ article }}</p>
  {% endfor %}

  <a href="{% url "articles:index" %}">[back]</a>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>  
    // 1. 팔로우 선택
    const formTag = document.querySelector("#follow-form")
    // 7. csrf_token 선택 (공식문서 참고)
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    // 2. 팔로우 버튼에 이벤트 리스너를 부착 (submit 이벤트 감지)
    formTag.addEventListener('submit', function (event) {
      // 3. submit 이벤트의 기본 동작 취소
      event.preventDefault()
      // 5. HTML에서 준비한 user의 pk를 조회
      // 3가지 방식이 존재함
      // console.log(event.currentTarget.dataset.userId)
      const userId = event.currentTarget.dataset.userId
      // const userId = this.dataset.userId
      // const userId = formTag.dataset.userId
      // 4. axios 준비
      axios({
        method: 'post',
        // 6. HTML에서 전달해서 할당한 값으로 url 완성
        url: `/accounts/${userId}/follow/`,
        // 8. 선택한 csrf_token값을 요청 headers에 세팅! (공식문서) 
        // -> axios에서 headers를 쓰는지 확인하기
        headers: {'X-CSRFToken': csrftoken},
      })
        .then((response) => {
          console.log(response)
          // 11. django로 부터 응답받은 팔로우 상태 정보
          console.log(response.data)
          // 12. 팔로우 상태 정보 데이터에 따라 팔로우 
          const isFollowed = response.data.is_followed
          const followBtn = document.querySelector('.follow-input')
          if (isFollowed === true) {
            followBtn.value = '언팔로우'
          } else {
            followBtn.value = '팔로우'
          }
          // 13. 팔로워 & 팔로잉 수 선택
          const followingsCountTag = document.querySelector('#followings-count')
          const followersCountTag = document.querySelector('#followers-count')

          // 15. django가 응답한 팔로잉, 팔로워 수 데이터를 활용해 DOM 변경
          followingsCountTag.textContent = response.data.followings_count
          followersCountTag.textContent = response.data.followers_count
        })
        .catch((error) => {
          console.log(error)
        })
    })
  </script>
</body>
</html>
```

```python
# accounts/views.py
def follow(request, user_pk):
    User = get_user_model()
    you = User.objects.get(pk=user_pk)
    me = request.user

    if me != you:
        # 9. JS에게 팔로우 상태여부를 전달할 데이터
        if me in you.followers.all():
            you.followers.remove(me)
            # me.followings.remove(you)
            is_followed= False
        else:
            you.followers.add(me)
            # me.followings.add(you)
            is_followed = True
        context = {
            'is_followed' : is_followed,
            # 14. 팔로워 & 팔로잉 수 선택
            'followings_count' : you.followings.count(),
            'followers_count' : you.followers.count(),
        }
        # 10. JSON 데이터로 응답
        return JsonResponse(context)
        
    return redirect('accounts:profile', you.username)
```

## Ajax with likes

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Articles</h1>

  {% if request.user.is_authenticated %}
    <p>안녕하세요 {{ user.username }}</p>
    <a href="{% url "accounts:profile" user.username %}">내 프로필</a>

    <a href="{% url "articles:create" %}">CREATE</a>
    <form action="{% url "accounts:logout" %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="LOGOUT">
    </form>
    <form action="{% url "accounts:delete" %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="회원탈퇴">
    </form>
    <a href="{% url "accounts:update" %}">회원정보 수정</a>
  {% else %}
    <a href="{% url "accounts:login" %}">LOGIN</a>
    <a href="{% url "accounts:signup" %}">회원가입</a>
  {% endif %}

  <article class="article-container">
    {% for article in articles %}
    <a href="{% url "accounts:profile" article.user.username %}">
      <p>작성자: {{ article.user.username }}</p>
    </a>
    <p>글 번호: {{ article.pk }}</p>
    <a href="{% url "articles:detail" article.pk %}">
      <p>글 제목: {{ article.title }}</p>
    </a>
    <p>글 내용: {{ article.content }}</p>
    {% comment %} 좋아요 form 버튼 {% endcomment %}
    {% comment %} 6. 좋아요 버튼에 action과 method 삭제 {% endcomment %}
    {% comment %} 9. JS에 전달할 data속성 설정 {% endcomment %}
    <form data-article-id="{{ article.pk }}">
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
      {% comment %} 17. 각 좋아요 버튼을 구별할 수 있는 id 속성 추가 {% endcomment %}
        <input type="submit" value="좋아요 취소" id="like-{{ article.pk }}">
      {% else %}
        <input type="submit" value="좋아요" id="like-{{ article.pk }}">
      {% endif %}
    </form>
    <hr>
    {% endfor %}
  </article>

  {% comment %} 1. axios CDN 작성 {% endcomment %}
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  
  <script>
    // 2. 게시글을 모두 포함하는 최상위 요소를 선택
    const articleContainer = document.querySelector('.article-container')
    // 7. csrf_token
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    // 3. 선택한 최상위 요소에 이벤트 헨들러를 부착
    articleContainer.addEventListener('submit', function (event) {
      // 4. submit 이벤트 기본 동작 취소
      event.preventDefault()
      //10. HTML에서 전달한 게시글 id 받기
      const articleId = event.target.dataset.articleId
      // 5. axios 요청 작성
      axios({
        method: 'post',
        // 11. 전달 받은 게시글 ud로 url완성
        url: `/articles/${articleId}/likes/`,
        // 8. 선택한 csrf_token headers에 부착
        headers: {'X-CSRFToken': csrftoken},
      })
        .then((response) => {
          console.log(response)
          console.log(response.data)
          // 14. django한테 응답 받은 좋아요 상태 정보 저장
          const isLiked = response.data.is_liked
          // 16. 좋아요 버튼 선택
          const likeBtn = document.querySelector(`#like-${articleId}`)
          // 15. 좋아요 상태 정보에 따라 버튼 변경
          if (isLiked === true){
            likeBtn.value = '좋아요 취소'
          } else {
            likeBtn.value = '좋아요'
          }
        })
        .catch((error) => {
          console.log(error)
        })
    })
  </script>

</body>
</html>

```

```python
@login_required
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    article = Article.objects.get(pk=article_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article.pk)

from django.http import JsonResponse
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    # 12. 좋아요 상태여부를 JS에 응답할 데이터 세팅
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        is_liked = False
    else:
        article.like_users.add(request.user)
        is_liked = True
    # 세팅한 데이터를 Json 형태로 응답
    context = {
        'is_liked': is_liked,
    }
    return  JsonResponse(context)
```
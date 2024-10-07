# Django_08(Authentication System 01)

날짜: 2024년 9월 30일

# Cookie & Session

## HTTP

HTML 문서와 같은 리소스들이 가져올 수 있도록 해주는 규약, 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초

1. 비 연결 지향(connetionless)
    - 서버는 요청에 응답을 보낸 후 연결을 끊음
2. 무상태(stateless)
    - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
        - 장바구니에 담은 상품을 유지할 수 없음
        - 로그인 상태를 유지할 수 없음

## 쿠키(Cookie)

서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

- 서버가 제공하여 클라이언트 측에서 저장되는 작은 데이터 파일
- 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식

### 쿠키 동작 예시

1. 브라우저가 웹 서버에 웹 페이지를 요청
2. 웹 서버는 요청된 페이지와 함께 쿠키를 포함한 응답을 브라우저에게 전송
3. 브라우저 받은 쿠키를 저장소에 저장 + 쿠키의 속성(만료 시간, 도메인, 주소 등)도 함께 저장됨
4. 이후 브라우저가 같은 웹 서버에 웹 페이지를 요청할 때, 저장된 쿠키 중 해당 요청에 적용 가능한 쿠키를 포함하여 함께 전송
5. 웹 서버는 받은 쿠키 정보를 확인하고, 필요에 따라 사용자 식별, 세션 관리 등을 수행
6. 웹 서버는 요청에 대한 응답을 보내며, 필요한 경우 새로운 쿠키를 설정하거나 기존 쿠키를 수정할 수 있음

### 쿠키의 작동 원리와 활용

1. 쿠키 저장 방식
    - 브라우저(클라이언트)는 쿠키를 KEY-VALUE의 데이터 형식으로 저장
    - 쿠키에는 이름, 값 외에도 만료 시간, 도메인, 경로 등의 추가 속성이 포함 됨
2. 쿠키 전송 과정
    - 서버는 HTTP 응답 헤더의 Set-Cookie 필드를 통해 클라이언트에게 쿠키를 전송
    - 브라우저는 받은 쿠키를 저장해 두었다가, 동일한 서버에 재요청 시 HTTP 요청
    - Header의 Cookie 필드에 저장된 쿠키를 함께 전송
3. 쿠키의 주요 용도
    - 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨
    - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
    - 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억시켜 주는 역할

⇒ 서버에게 “나 로그인된 사용자야!”라는 인증 정보가 담긴 쿠키를 매 요청마다 계속 보내는 것

### 쿠키 사용 목적

1. 세션 관리(Session management)
    - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리
2. 개인화 (Personalization)
    - 사용자 선호 설정(언어 설정, 테마 등) 저장
3. 트래킹 (Tracking)
    - 사용자 행동을 기록 및 분석

## 세션(Session)

서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지 + 상태 정보를 저장하는 데이터 저장 방식

→ 쿠케에 세션 데이터를 저장하여 매 요청시마다 세션 데이터를 함께 보냄

### 세션 작동 원리

1. 클라이언트가 로그인 요청 후 인증에 성공하면 서버가 session 데이터를 생성 후 저장
2. 생성된 session 데이터에 인증 할 수 있는 session id를 발급
3. 발급한 session id를 클라이언트에게 응답( 데이터는 서버에 저장, 열쇠만 주는 것)
4. 클라이언트는 응답 받은 session id를 쿠키에 저장
5. 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠기(session id가 저장된)를 서버에 전달
6. 쿠키는 요청 때마다 서버에 함께 전송 되므로 서버에서 session id를 확인해 로그인 되어있다는 것을 계속해서 확인하도록 함

⇒ 서버 측에서는 세션 데이터틀 생성 후 저장하고 이 데이터에 접근할 수 있는 세션 ID를 생성 → 이 ID를 클라이언트 측으로 전달하고, 클라이언트는 쿠키에 이 ID를 저장 → 이후 클라이언트가 같은 서버에 재요청 시마다 저장해 두었던 쿠키도 요청과 함께 전송

(ex) 예를 들어 로그인 상태 유지를 위해 로그인 되어있다는 사실을 입증하는 데이터를 매 요청마다 계속해서 보내는 것

## 쿠키와 세션의 목적

클라이언트와 서버 간의 상태 정보를 유지하고 사용자를 식별하기 위해 사용

# Django Authentication System

사용자 인증과 관련된 기능을 모아 놓은 시스템 

## Authentication(인증)

사용자가 자신이 누구인지 확인하는 것 (신원 확인)

### 사전 준비

- 두 번째 app accounts 생성 및 등록
- auth와 관련한 경로나 키워드들을 django 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 되도록 ‘accounts’로 사용하는 것을 권장

## Custom User model

### 기본 User Model의 한계

- 우리는 지금까지 별도의 User 클래스 정의 없이 내장된 auth 앱에 작성된 User 클래스를 사용했음
- Django의 기본 User 모델은 username, password 등 제공되는 필드가 매우 제한적
- 추가적인 사용자 정보(예: 생년월일, 주소, 나이 등)가 필요하다면 이를 위해 기본 User Model을 변경하기 어려움
    - 별도의 설정 없이 사용할 수 있어 간편하지만, 개발자가 직접 수정하기 어려움
- 내장된 auth 앱 → 이게 User model을 갖고 있음!
    
    ```python
    # crud/settings.py
    INSTALLED_APPS = [
        'articles',
        'accounts',
        'django_extensions',
        'django.contrib.admin',
        'django.contrib.auth',      # 이놈 자식!!!!
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    
    ```
    

### User Model 대체의 필요성

- 프로젝트의 특정 요구사항에 맞춰 사용자 모델을 확장할 수 있음
- 예를 들어 이메일을 username으로 사용하거나, 다른 추가 필드를 포함시킬 수 있음

### Custom User Model로 대체하기

- AbstractUser 클래스를 상속받는 커스텀 User 클래스 작성
    
    → 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 기존 User 클래스와 완전히 같은 모습을 가지게 됨
    

```python
# accounts.models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# 커스텀 User 모델로 대체하기 위한 class 작성
class User(AbstractUser):
    pass
```

- django 프로젝트에서 사용하는 기본 User 모델을 우리가 작성한 User 모델로 사용할수 있도록 AUTH_USER_MODEL 값을 변경
    - 수정 전 기본 값은 ‘auth.User’

```python
# crud/settings.py
AUTH_USER_MODEL = 'accounts.User'
```

- admin site에 대체한 User 모델 등록
    - 기본 User 모델이 아니기 때문에 등록하지 않으면 admin 페이지에 출력되지 않기 때문

```python
# accounts/admins.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)
```

### AUTH_USER_Model

Django 프로젝트의 USER를 나타내는 데 사용하는 모델을 지정하는 속성 

- 주의

**프로젝트 중간에 AUTH_USER_MODEL을 변경 할 수 없음**

→ 이미 프로젝트가 진행되고 있을 경우 데이터베이스 초기화 진행

![image.png](image.png)

- auth-user → accounts_user로 변경된 것을 확인할 수 있음!

### 프로젝트를 시작하며 반드시 User 모델을 대체해야 한다.

- Django는 새 프로젝트를 시작하는 경우 비록 기본 User 모델이 충분하더라도 커스텀 User 모델을 설정하는 것을  강력하게 권장하고 있음
- 커스텀 User 모델은 기본 User 모델과 동일하게 작동(1) 하면서도 필요한 경우 나중에 맞춤 설정(2)할 수 있기 때문
- 단, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 맞춰야 함

## Login

로그인은 Session을 Create하는 과정

### AuthenticationForm()

로그인 인증에 사용할 데이터를 입력 받는 built-in form

```bash
$ python manage.py createsuperuser
Username: admin
Email address: 
Password: 1234
Password (again): 1234
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

1. accounts/urls.py 

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    
]
```

1. accounts/views.py
- 인증시스템에 대한 Form은 미리 구현되어있음
- login(request, user) : AuthenticationForm을 통해 인증된 사용자를 로그인 하는 함수
- get_user() : AuthenticationForm의 인스턴스 메서드
    - 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def login(request) :
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST) # ModelForm이 아닌 Form을 사용하고 있음, 그래서 인자 구성이 다름!
        if form.is_valid() :
            # 만약 인증된 사용자라면 로그인 진행 (세션 데이터 생성)
            # auth_login(request, 인증된 유저 객체)
            auth_login(request, form.get_user())
            return redirect('articles:index')
            
    else : 
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)
```

1. accounts/login.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>로그인</h1>
    <form action="{% url "accounts:login" %}" method="POST">
        {% csrf_token %}
        {{ form.as_p}}
        <input type="submit" value='로그인'>
    </form>
</body>
</html>
```

1. articles/index.py

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <p>안녕하세요 {{ user.username }}</p>
  <h1>Articles</h1>
  <a href="{% url "accounts:login" %}">Login</a>
```

### 세션 데이터 확인하기

![image.png](image%201.png)

## Logout

로그아웃은 Session을 Delete하는 과정

### logout(request)

1. DB에서 현재 요청에 대한 Session Data를 삭제
2. 클라이언트의 쿠키에서도 Session Id를 삭제

### 로그아웃 로직 작성

1. accounts/urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]

```

1. articles/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <p>안녕하세요 {{ user.username }}</p>
  <h1>Articles</h1>
  <a href="{% url "accounts:login" %}">Login</a>
  # 여기에 logout 기능 추가 #
  <form action="{% url "accounts:logout" %}" method='POST'>
    {% csrf_token %}
    <input type="submit" value="LOGOUT">
  </form>
  <a href="{% url "articles:create" %}">CREATE</a>
  {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <a href="{% url "articles:detail" article.pk %}">
      <p>글 제목: {{ article.title }}</p>
    </a>
    <p>글 내용: {{ article.content }}</p>
    <hr>
  {% endfor %}

</body>
</html>

```

1. accounts/views.py

```python

def logout(request):
    # 세션 데이터 삭제
    auth_logout(request)
    return redirect('articles:index')
```

# Template with Authentication data

템플릿에서 인증 관련 데이터를 출력하는 방법

### 현재 로그인 되어있는 유저정보 출력하기

user라는 context 데이터를 사용할 수 있는 이유는?

→ django가 미리 준비한 context 데이터가 존재하기 때문(context processeors) 

### context processors

- 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
- 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨
    
    → django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해 둔 것
    

# 참고

## 쿠키의 수명

### 쿠키 종류별 Lifetime (수명)

1. Session cookie
    - 현재 세션이 종료되면 삭제됨
    - 브라우저종료와 함께 세션이 삭제됨
2. Persistent cookies
    - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

## 쿠키와 보안

### 쿠키의 보안 장치

- 제한된 정보
    - 쿠키에는 보통 중요하지 않은 정보만 저장 (사용자 ID나 세션 번호 같은 것)
- 암호화
    - 중요한 정보는 서버에서 암호화해서 쿠키에 저장
- 만료 시간
    - 쿠키에는 만료 시간을 설정 시간이 지나면 자동으로 삭제
- 도메인 제한
    - 쿠키는 특정 웹사이트에서만 사용할 수 있도록 설정할 수 있음

### 쿠키와 개인정보 보호

- 많은 국가에서 쿠키 사용에 대한 사용자 동의를 요구하는 법규를 시행
- 웹사이트는 쿠키 정책을 명시하고, 필요한 경우 사용자의 동의를 얻어야 함

## Django에서의 세션 관리

### 세션 in Django

- Django는 ‘database-backed sessions’ 저장 방식을 기본 값으로 사용
- session 정보는 DB의 django_session 테이블에 저장
- Django는 요청안에 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session 데이터를 알아냄
    
    → Django는 우리가 session 메커니즘(복잡한 동작원리)에 대부분을 생각하지 않게끔 많은 도움을 줌
    

## AbstractUser class

“관리자 권한과 함께 완전한 기능을 가지고 있는 user model을 구현하는 추상 기본 클래스”

- 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
- 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가 됨
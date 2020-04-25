## CRUD-views.py

### 2. views.py - 함수 정의

- urls.py를 통해 정의된 urlpattern에 따라, 요청이 들어오면 어떤 것을 반환할건지에 대한 기본 로직을 작성하는 파일임. 함수로 정의되며, 함수의 인자로 `request`를 받음
- 함수 `render`첫번째 인자로 `request`를 넘겨주고, 어떠한 html 을 보여줄건지를 설정함.
- return 으로 반환되는 `render` 함수의 첫 번째 인자 `request`는 위 index 함수의 첫번째 인자와 동일함.

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')

def update(request, pk):
    # 수정시에는 해당 article 인스턴스를 넘겨줘야한다!
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

```



## Sign - views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_POST

from .forms import CustomUserChangeForm

# Create your views here.
def signup(request):
    # 로그인이 되어있다면,
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 게시글 목록 페이지
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        # 사용자가 보낸 값 -> form
        form = AuthenticationForm(request, request.POST)
        # 검증
        if form.is_valid():
            # 검증 완료시 로그인!
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    # 조건식으로 직접 작성 해도 된다.
    auth_logout(request)
    return redirect('articles:index')

@require_POST
@login_required
def delete(request):
    request.user.delete()
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)
```



## sign-form.py

```python
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

# 그대로 활용하지 못하는 경우는 항상 상속받아서 custom!!!!
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']
```



## review-form.py

```python
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']
```





## urls.py

- ### 1. urls.py - url 패턴 정의

  - urlpatterns 라는 리스트안에 주소를 하나하나씩 쌓아 넣음.
    - 첫번째 인자: URL 주소를 입력
    - 두번째 인자: 해당 URL 주소로 요청이 들어올 때 views.py 내 연결할 함수를 입력함. 이 함수는 어플리케이션 폴더 내 views.py에 작성되어있으므로 `import` 해와야함 예) `from pages import views`

  > 아래 코드에서 입력한 내용의 의미는 다음과 같다. `index/` 라는 url로 요청이 들어온, 두번째 인자의 내용에 따라, views.py 내 `index` 함수를 실행함. views.py이 함수를 통해 return 되는 값을 반환하는데, 그 결과 값은 index.html을 render 하는 것임

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
]
```



## models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



## admin.py

```python
from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at', )

# 어드민 사이트에 등록해줘
admin.site.register(Article, ArticleAdmin)
```



## static

```python
# serving 되는 URL 앞에 붙음.
STATIC_URL = '/static/'
# app 디렉토리가 아닌 static 폴더 지정
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```



## main urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls'))
]
```



## new.html

```html
{% extends 'base.html' %}
{% load static %}
{% block css %}
<link rel="stylesheet" href="{% static 'stylesheets/form.css' %}">
{% endblock %}

{% block body %}
    <h2>글쓰기</h2>
    <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        <label for="title">제목 : </label>
        <input type="text" name="title" id="title" autofocus required> <br>
        <label for="content">내용 : </label>
        <textarea name="content" id="content"></textarea>
        <input type="submit" value="작성완료">
    </form>
{% endblock %}
```



## index.html

```html
{% extends 'base.html' %}

{% block body %}
    <h2>게시판</h2>
    <a href="{% url 'articles:new' %}">글쓰기</a>
    {% for article in articles %}
        <p>{{ article.id }}</p>
        <p>{{ article.title }}</p>
        <a href="{% url 'articles:detail' article.pk %}">글 보러가기</a>
        <hr>
    {% endfor %}
{% endblock %}
```



## edit.html

```html
{% extends 'base.html' %}

{% block body %}
<h2>{{ article.pk }}번 글 수정하기</h2>
<form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    <label for="title">제목 : </label>
    <input type="text" name="title" id="title" value="{{ article.title }}" autofocus required> <br>
    <label for="content">내용 : </label>
    <textarea name="content" id="content">{{ article.content }}</textarea>
    <input type="submit" value="작성완료">
</form>
{% endblock %}
```



## detail.html

```html
{% extends 'base.html' %}

{% block body %}
    <h1>{{ article.pk }}번 글</h1>
    <h2>{{ article.title }}</h2>
    <p>생성 : {{ article.created_at }}</p>
    <p>수정 : {{ article.updated_at }}</p>
    <hr>
    <p>{{ article.content }}</p>
    <form action="{% url 'articles:delete' article.pk %}" method="POST" class="d-inline">
        {% csrf_token %}
        <button class="btn btn-primary">삭제</button>
    </form>
    <a href="{% url 'articles:update' article.pk %}"><button class="btn btn-primary">수정</button></a>
{% endblock %}

```



### 로그인 & 세션

세션이란, 웹 서버에서 임시로 클라이언트의 데이터를 갈무리하는 것을 뜻한다. 쿠키와 비슷한 역할이나, 쿠키는 클라이언트 측에 데이터를 갈무리 하는 반면에, 세션은 서버측에 데이터를 갈무리한다는 차이점이 있다. 주로 로그인, 온라인 쇼핑몰의 장바구니 등에 쓰인다 ([나무위키](https://namu.wiki/w/세션))

웹 브라우저와 서버가 HTTP 프로토콜을 통해서 하는 모든 커뮤니케이션은 무상태(stateless)라고 합니다. 프로토콜이 무상태라는 뜻은 클라이언트와 서버 사이의 메시지가 완벽하게 각각 독립적이라는 뜻입니다. 여기엔 이전 메시지에 근거한 행동이나 순서(sequence)라는 것이 존재하지 않습니다. 결국, 만약 사이트가 클라이언트와 계속적인 관계를 유지하는 것을 당신이 원한다면, 당신이 직접 그 작업을 해야합니다.

세션이라는 것은 Django 그리고 대부분의 인터넷에서 사용되는 메카니즘으로, 사이트와 특정 브라우저 사이의 “state”를 유지시키는 것입니다. 세션은 당신이 매 브라우저마다 임의의 데이터를 저장하게 하고, 이 데이터가 브라우저에 접속할 때 마다 사이트에서 활용될 수 있도록 합니다. 세션에 연결된 각각의 데이터 아이템들은 “key”에 의해 인용되고, 이는 또다시 데이터를 찾거나 저장하는 데에 이용됩니다. ([장고 튜토리얼](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Sessions))

장고 서버는 우리가 접속하고 있는 브라우저의 정보를 임시로 가지고 있음. 따라서 어떤 클라이언트가 어떤 페이지를 보고 있는지 등의 정보를 장고에서 알 수 있음. 로그인의 경우, 마치 파이썬에서 사용한 글로벌 변수처럼, 일반적으로 페이지를 이동하더라도 유지되어야 함. 우리는 세션을 이용하여 페이지가 이동하더라도 유지되도록, 로그인 기능을 구현할 수 있음.

- `AuthenticationForm` : 유저가 존재하는지를 검증하는 Django 내장 모델 폼. 사용자가 로그인 폼에 작성한 정보가 유효한지를 검증함
- `auth_login`(default:`login`)
  - 유저 정보를 세션에 생성 및 저장하는 역할을 하는 Django 내장 함수.
  - `login_form.get_user()` 를 통해 `login_form`에 저장된 유저 정보를 갖고와 세션에 유저 정보를 생성함
  - ***`AuthenticationForm` 은 유저가 존재하는지를 검증할 뿐, 세션과는 무관함을 유의하자.\***

- Static Web : HTML & CSS 등으로만 구성된 정말 단순한 웹서비스
  - 이문서를 주세요 라고 요청하면, 어떠한 변형, 연산등도 없이, 단순히 문서를 보냄(응답). 서버의 파일이 도서관의 책처럼 적재되어 있고 클라이언트의 요청을 통해서해당 파일을 마치 책을 보는 것처럼 꺼 내 올 수만 있는 웹 서비스.
- Dynamic Web(Web Application program)
  - Static Web과 상반되는 개념. 동적으로파일을 생성하여 뿌려주는 Web. 장고는 Dynamic web이라고 하는 내부적으로 연산도 가능하고, 사용자의 인풋마다 다른 아웃풋을 보여주는 동적웹임.



### Model

- 안전하게 데이터를 저장

- DB 관련된 코드를 작성하는 곳. 어플리케이션(예; pages)에서 사용할 DB를 정의함. 어떠한 데이터베이스 테이블을 만들건지 등을 정의하는 곳.



### View

- 데이터를 적절하게 유저에게 보여줌

- 어떠한 요청이 들어왔을 때, 무엇을 실행할건지? 우리가 보게될 페이지를 만드는 곳? 페이지들이 모여있는 곳임.



### Control , Template(Django)

-  사용자의 입력과 이벤트에 반응하여 Model 과 View 를 보여주기위한 것 html로 작성



# Variable routing

> URL 주소자체를 변수로 사용하는것을 의미함. URL 주소로 들어오는 값을 변수로 지정하여, views.py 내 함수의 인자로 넘겨줌. 변수값에 따라 다른 페이지를 연결 시킬 수 있음.

- urls.py
  - 페이지를 접근하는 주소를 urls.py에 생성.
  - 기본적으로 `< >`의 형태로 variable routing을 정의함
    - `` 은 자료의 형태를 string(문자열)으로 제한한다는 의미임.
    - `<>` 내 변수가 views.py 내 함수의 인자로 할당됨
  - 예를들어, `기본주소/hello/harry` 와 같은 예시의 주소를 요청하면, `name` 변수의 값으로 harry가 할당되며, 이 값을 views.py 및 render 되는 html 파일에서 사용 할 수 있게 됨.

```python
urlpatterns = [
    path('hello/<str:name>/', views.hello),
    path('admin/', admin.site.urls),
]

def hello(request, name):
    return render(request, 'hello.html', {'name': name})
```



### Migrations

- Django에서 Model 클래스를 생성하고 난 후, 해당 모델에 상응하는 테이블을 데이터베이스에서 생성할 수 있음. Python 모델 클래스를 DB에 적용하는 과정을 Migration이라고 함.
- 모델의 변경 내역을 DB Schema(데이터베이스 데이터 구조)로 반영시키는 효율적인 방법을 제공.
  - `python manage.py makemigrations` : 마이그레이션 파일(초안) 생성
  - `python manage.py migrate` : 해당 마이그레이션 파일을 실제 데이터 베이스에 반영(적용)
- 모델 클래스 생성 후, 위의 명령어를 반드시 입력해야, 데이터를 입력하기 위한 Schema가 DB에 반영됨.



### CSRF

> CSRF: 사이트 간 요청 위조(Cross-site Request Forgery)
>
> 웹 애플리케이션 취약점 중 하나로 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 한다거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

- CSRF 토큰이란 CSRF 공격에 대응을 하기 위한 방어 기법 중 하나임. 보통 CSRF공격은 특정액션시 넘어가는 파라미터를 가지고 그 행위를 특정액션 이외에 자동으로 넘어가게 하는 기법인데 이것을 넘어가는 값 중에 랜덤으로 발행되는 키값을 넘기고 받게 해서 이 값이 일치하지 않으면 그 액션을 수행하지 않는 것이다.
- CSRF token은 보안상의 목적으로 사용. token을 넣어줘야 token과 함께 `create` 페이지에 요청을 보냄. 장고에서 csrf token을 가지고, 피하식별 하듯이, 우리 사이트에서 보낸 요청이라는 것을 확실히 알 수 있게 됨.
- Post 메소드를 쓸 때는 반드시 `csrf_token`이 있어야함.



### resolver_match

```html
{% if request.resolver_match.url_name == 'create' %}
        <h2>새 글쓰기</h2>
    {% else %}
        <h2>수정하기</h2>
    {% endif %}
```



하드코팅 url 지우기

https://tothefullest08.github.io/django/2019/04/27/Django08_template_hardcoding_delete/

모델폼

https://tothefullest08.github.io/django/2019/04/27/Django13_Django_Model_Form/

# Form vs Model Form

**모델 폼과 폼의 가장 핵심적인 차이점은 모델(모델 클래스)과의 연동 유무임.**

- 폼은 모델과 연동이 되어있지 않기 때문에, `request.POST` 로 들어오는 `input` 에 대한 정보를 선별하여 각 변수에 저장하고 DB에 생성 및 저장을 해야함.
- 그러나, 모델 폼의 경우, 모델과 연동이 되어있기 때문의 위의 과정을 거칠 필요 없이 DB에 저장만 하면됨.



get_object_or_404

- url 주소로 이미 삭제 된 id를 이용하려는 접근할 경우 에러가 발생함.
- 존재 하지 않는 id 값 기반의 url 주소로 접속할 경우, 에러가 발생하므로 `Movie.objects.get` 대신 `get_object_or_404` 를 사용하여 404 에러 메세지(Page not found)를 표시하게 코드 작성(사용자 친화적)
- 사용을 위해 import 해올 것. `from django.shortcuts import get_object_or_404`
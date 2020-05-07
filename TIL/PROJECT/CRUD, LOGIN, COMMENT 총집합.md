# CRUD, LOGIN, COMMENT 총집합

### Template 상속, 기본 세팅



1. django_pjt3

* settings.py

```python
import os

#모든 호스트가 읽게 허락
ALLOWED_HOSTS = ["*"]


#앱 등록시 설정해줘야 한다. bootstrap4도 사용하려면 등록해줘야 한다.
INSTALLED_APPS = [
   ...
    'community',
    'accounts',
    'bootstrap4',
]


 # base.html 템플릿 상속을 위해 BASE_DIR에서 템플릿 인식하게 연결하기.
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'django_pjt3', 'templates')],
        ...
            ],
        },
    },
]

# 한국어, 한국시간 설정
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'




```

* urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('community/', include('community.urls')),
    path('accounts/', include('accounts.urls')),
]
```

* templates/base.html

       상속받을 템플릿들이 정의될 공간.
       {% block body %}
        {% endblock %} 
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand font-weight-bold mx-3" href="{% url 'community:review_list' %}">MovieReviews</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav ml-auto">

      {% if request.user.is_authenticated %}
      <li class="nav-item active ">
        <a class="nav-link text-decoration-none" href="#">{{user.username}}님 환영합니다.</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="{% url 'community:review_list' %}">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'community:create' %}">New</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'accounts:logout'%}">Logout</a>
      </li>
      {% else %}
       <li class="nav-item active">
        <a class="nav-link" href="{% url 'community:review_list' %}">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'community:create' %}">New</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'accounts:login'%}">Login</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'accounts:signup'%}">Signup</a>
      </li>
      {% endif %}
    </ul>
  </div>
</nav>

    <div class=m-3>
       
        {% block body %}
        {% endblock %}
    </div>

    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>
```

---

### CRUD + COMMENT



2. community

* urls.py

```python
from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_list, name= 'review_list'),
    path('<int:review_pk>/', views.detail, name= 'detail'),
    path('create/', views.create, name= 'create'),
    path('<int:review_pk>/update/', views.update, name= 'update'),
    path('<int:review_pk>/delete/', views.delete, name= 'delete'),
    path('<int:review_pk>/comments/', views.comment_create, name= 'comment_create'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name= 'comment_delete'),


]

```

* models.py

```python
from django.db import models
from django.conf import settings

# 게시글 작성할 모델
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=30)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#게시글에 댓글 모델
class Comment(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   review = models.ForeignKey(Review, on_delete=models.CASCADE)
   content = models.CharField(max_length=200)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

```

* forms.py

`field = '__all__'`설정하면 모델의 모든 속성을 필드로 등록 가능

```python
from django import forms
from .models import Review, Comment

#게시글 폼
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title','movie_title','content','rank']

#댓글 폼
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

```

* admin.py

필수는 아니다. 하지만 등록하면 admin사이트에서 CRUD가능.

```python
from django.contrib import admin
from .models import Review

# Register your models here.
admin.site.register(Review)
```

* views.py

`is_authenticated` : 로그인 여부 확인

`reviews = Review.objects.all().order_by('-pk')` : 모든 리뷰내역을 가져와서, pk값 내림차순에 따라 정렬

`get_object_or_404(Review, pk=review_pk)` : get방식으로 Review모델에서 pk=review_pk값을 가져오고 에러가 있으면 404(사용자 에러)를 보여줌

`save(commit=False)` : save()는 바로 DB에 저장해버리기 때문에 commit=False하면 db에는 저장되지 않는다.

```python
#get_object_or_404 : GET방식으로 가져오고 잘못되면 404(사용자에러)에러를 보여줌
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review,Comment
from .forms import ReviewForm,CommentForm
#로그인 필수로 요구됨
from django.contrib.auth.decorators import login_required
#포스트 방식이 필수로 요구됨
from django.views.decorators.http import require_POST


#리뷰 리스트를 보여주는 index페이지 역할에 적용
def review_list(request):
    # 모든 리뷰내역을 가져와서, pk값 내림차순에 따라 정렬한다.
    reviews = Review.objects.all().order_by('-pk')
    context = {
        'reviews': reviews
    }
    return render(request, 'community/review_list.html',context)

# 상세 게시글을 보여주는 역할
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm()
    context = {
        'review':review,
        'comment_form' : comment_form
    }
    return render(request, 'community/review_detail.html', context)

# 새글쓰기 역할. 로그인이 요구된다.
@login_required
def create(request):
    #Post방식
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        # 폼 유효성 검사를 한다. (폼 안에 모든 값이 제대로 들어갔는지)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:review_list')
    else:
        #GET방식. 
        review_form = ReviewForm()
    # GET 방식이거나, POST 방식이어도 유효성 검사가 실패하면 form.html로 넘긴다.
    context = {
        'review_form' : review_form
    }
    return render(request,'community/form.html',context)

# 글 수정 기능
@login_required
def update(request, review_pk):
    #로그인 되어있다면
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        # 작성자 == 수정 요청자이면 수정허락. 아니면 게시글상세페이지로 보냄
        if review.user != request.user:
            return redirect('community:detail', review.pk)
        else :
            if request.method == "POST":
                review_form = ReviewForm(request.POST, instance=review)
                if review_form.is_valid():
                    updated = review_form.save()
                    return redirect('community:detail', updated.pk)
            else :
                review_form = ReviewForm(instance=review)
            context = {
                'review_form' : review_form
            }
            return render(request,'community/form.html', context)
    else:
        return redirect('accounts:login')

# 글 삭제 -> 무조건 요청을 POST방식으로 보내야한다.(@require_POST때문. 그리고 GET방식으로 url삭제가 가능하면 아무나 글을 삭제해버릴 수 있기 때문에 POST방식으로 해야!!)
@login_required
@require_POST
def delete(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.user != request.user:
            return redirect('community:detail', review.pk)
        else:
            if request.method == "POST":
                review = get_object_or_404(Review, pk=review_pk)
                review.delete()
                return redirect('community:review_list')
            else :
                return redirect('community:detail', review.pk)

    else:
        return redirect('accounts:login')

# 댓글달기 기능
@login_required
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # save()는 바로 DB에 저장해버리기 때문에 user정보를 저장하지도 못한채로 저장되버리게 되어 user(FK)에 대해 NOT NULL 무결성에러가 발생. 그래서 commit=false로 db에는 보내지 않고 user정보를 저장한 후 save하여 db에 보낸다.form의 정보를 comment에 담은 후 user정보까지 저장해서 마지막으로 save함.
        
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
        return redirect('community:detail', review.pk)


# 댓글 삭제 마찬가지로 반드시 POST방식으로 요청되어야
@require_POST
def comment_delete(request, review_pk, comment_pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            comment = get_object_or_404(Comment, pk=comment_pk)
            if comment.user == request.user:
                comment.delete()
        return redirect('community:detail', review_pk)
    else :
        return redirect('accounts:login')
```

* form.html(새글쓰기, 수정하기)

`{% if request.resolver_match.url_name == 'create' %}`를 사용하여 요청 url의 이름에 따라 다른 화면을 보여주게 설정

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block body %}

{% if request.resolver_match.url_name == 'create' %}
<h3>새 글쓰기</h3>
<a href="{% url 'community:review_list' %}">BACK</a>
<form action="" method="POST">

{% else %}
<h3>수정하기</h3>
<a href="{% url 'community:review_list' %}">BACK</a>
<form action="" method="POST">
{% endif %}

{%csrf_token%}
{% bootstrap_form review_form %}
<button>SUMBIT</button>
</form>

{% endblock %}
```

* review_detail.html

```html
{% extends 'base.html' %}
{% load bootstrap4%}
{% block body %}


<h1 class="text-center my-5">영화 <{{review.movie_title}}></h1>
<div class="d-flex flex-column w-75 mx-auto">
<div class="card border-dark my-3">
    <div class="card-header display-5">
        <ul class="d-flex justify-content-between align-items-center mb-0">
            <h2>제목 : {{review.title}}</h2>
            <p>{{review.user.username}}님의 글</p>
        </ul>
    </div>
    <div class="card-body text-dark">
    <h4 class="card-text">{{review.content}}</h4>
    <hr/>
      <p class="card-text" style="color:slategrey">Rank: {{review.rank}}</p>
      <p class="card-text" style="color:slategrey">작성 시간: {{review.created_at}}</p>
      <p class="card-text" style="color:slategrey">업데이트 시간: {{review.updated_at}}</p>
    </div>
  </div>
    <div class="d-flex justify-content-center align-items-center ">
    <button><a  class="text-decoration-none" href="{% url 'community:review_list' %}" >BACK</a></button>
    {% if review.user == request.user %}
    <button class='mx-3'><a  class="text-decoration-none"  href="{% url 'community:update' review.pk %}">수정</a></button>
        <form action="{% url 'community:delete' review.pk %}"  method="POST">
            {% csrf_token %}
            <input type=submit value="삭제" style='color:red'>
        </form>
    {% endif %}
    
    </div>
    <div>
        <hr/>
    <h4>댓글 작성</h4>
    <hr/>
    <div class="mx-3">
        {% for comment in review.comment_set.all %}
        <p>{{comment.user.username}}님의 댓글 : {{comment.content}}</p>
        {% if request.user == comment.user %}
        <form action="{% url 'community:comment_delete' review.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <button class="">삭제</button>
        </form>
        {% endif %}
        <hr/>
        {% endfor %}
    </div>

    {% if user.is_authenticated %}
    <form action="{% url 'community:comment_create' review.pk %}" method="POST">
        {% csrf_token %}
        {% bootstrap_form comment_form %}
        <button>SUBMIT</button>
    </form>
    {% endif %}
    </div>

</div>




{% endblock %}
```

* review_list.html

```html
{% extends 'base.html' %}
{% block body %}

<h2 class="text-center">Movie Review Board</h2>
<a class="m-5" href="{% url 'community:create' %}">NEW</a>

<hr/>
<div>
<table class="table">
    <thead class="thead-dark">
      <tr>
        <th scope="col">#</th>
        <th scope="col">USER</th>
        <th scope="col">RANK</th>
        <th scope="col">MOVIE TITLE</th>
        <th scope="col">TITLE</th>
        <th scope="col">UPDATE</th>
        <th scope="col">DETAIL</th>


      </tr>
    </thead>
    <tbody>
    {% for review in reviews %}
      <tr>
        <th scope="row">{{ forloop.counter }}</th>
        <td>{{ review.user.username}}</td>
        <td>{{ review.rank}}</td>
        <td>{{review.movie_title}}</td>
        <td>{{ review.title}} [{{review.comment_set.count}}]</td>
        <td>{{ review.updated_at}}</td>
        <td><a href="{% url 'community:detail' review.pk %}">DETAIL</a></td>
      </tr>
    {% endfor %}

    </tbody>
  </table>
  <hr/>
  </div>

{% endblock %}
```

---

### LOGIN

`UserCreationForm`을 사용하여 회원가입 (장고내부에 정의된 폼을 사용할 수 있다.)

User < AbstractUser 상속관계에 있다. 우리는 안에 있는 User모델을 사용한다.

사용자 정의 Form을 만들어 사용할 수도 있다. (UserCreationForm을 상속받아 모델 정의해야함)

`AuthenticationForm`을 사용하여 로그인(장고내부에 정의됨)

__둘 다 장고 내부에 정의되어 있으므로 model(사용자지정안하면),form,admin 할 필요 없다__

* urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```

* models.py

```python
x
```

* forms.py

```python
x
```

* admin.py

```python
x
```

* views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def signup(request):
    if request.user.is_authenticated:

        return redirect('community:review_list')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:review_list')

    else:
        form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/signup.html', context)



def login(request):
    if request.user.is_authenticated:
        return redirect('community:review_list')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:review_list')

    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)

    return redirect('community:review_list')

```

* index.html(로그인, 회원가입)

`{% csrf_token %}` : 폼의 유효성 검사를 위해 꼭 필요. POST방식이면 꼭 위에 선언해줘야 csrf 유효성 검사 방식을 사용.

```html

{% extends 'base.html'%}
{% load bootstrap4 %}
{% block body %}

<div class='m-5'>
{% if request.resolver_match.url_name == 'login' %}
    <h3>로그인 페이지</h3>
<hr>
<form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <button>로그인</button>
{% else %}
    {% if request.resolver_match.url_name == 'login' %}
    <h3>회원가입 페이지</h3>
<hr>
<form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <button>회원가입</button>
{% endif %}
    <button><a class="tect-decoration-none" href="{% url 'community:review_list' %}">Back</a></button>
</form>
</div>
{% endblock %}
```


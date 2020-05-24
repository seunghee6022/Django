# 0513 Project4 code

### Path Tree

```python
django_pjt4
	django_pjt4
    	templates/base.html
    community   # CRUD 및 Comment(1:N), like(N:M) 	
    accounts    # login,logout,signup관련 기능, follow(N:M)   
```

---

### django_pjt4

* templates/base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://kit.fontawesome.com/7b6b66575b.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Movie Board</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand font-weight-bold mx-3" href="{% url 'community:index' %}">Movie Board</a>
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
        <a class="nav-link" href="{% url 'community:index' %}">Home</a>
      </li>

      <li class="nav-item">
        <a class="nav-link" href="{% url 'accounts:logout'%}">Logout</a>
      </li>
      {% else %}
       <li class="nav-item active">
        <a class="nav-link" href="{% url 'community:index' %}">Home</a>
      </li>

      <li class="nav-item">
        <a class="nav-link" href="{% url 'accounts:login'%}">Login</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'accounts:signup'%}">Signup</a>
      </li>
      {% endif %}


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

* settings.py

```python
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+0*=!=0t=-ia(t!$c#^!82dk$3whl_6bji6f&hybk%7ass(_)g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'community',
    'bootstrap4'
]

...

ROOT_URLCONF = 'django_pjt4.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'django_pjt4', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_pjt4.wsgi.application'

...

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
AUTH_USER_MODEL = 'accounts.User'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
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

---

### community

* urls.py

```python
from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:movie_pk>/review_list/', views.review_list, name= 'review_list'),
    path('<int:movie_pk>/create/', views.create, name= 'create'),
    path('<int:movie_pk>/<int:review_pk>/detail/', views.detail, name= 'detail'),
    path('<int:movie_pk>/<int:review_pk>/update/', views.update, name= 'update'),
    path('<int:movie_pk>/<int:review_pk>/delete/', views.delete, name= 'delete'),
    path('<int:movie_pk>/<int:review_pk>/comments/', views.comment_create, name= 'comment_create'),
    path('<int:movie_pk>/<int:review_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name= 'comment_delete'),
    path('<int:movie_pk>/<int:review_pk>/like/', views.like, name="like"),
]
```

* views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies,
    }
    return render(request, 'community/index.html',context)

def review_list(request,movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
        'movie': movie,
    }
    return render(request, 'community/review_list.html', context)

# @login_required
def create(request, movie_pk ):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()

            return redirect('community:review_list', movie.pk)
    else:
        review_form = ReviewForm()
    context = {
        'review_form' : review_form,
        'movie':movie,

    }
    return render(request,'community/form.html',context)

def detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm()
    context = {
        'movie':movie,
        'review':review,
        'comment_form' : comment_form,
    }
    return render(request, 'community/review_detail.html', context)


def update(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.user != request.user:
            return redirect('community:detail', movie.pk, review.pk)
        else :
            if request.method == "POST":
                review_form = ReviewForm(request.POST, instance=review)
                if review_form.is_valid():
                    updated = review_form.save()
                    return redirect('community:detail', movie.pk, updated.pk)
            else :
                review_form = ReviewForm(instance=review)
            context = {
                'movie':movie,
                'review_form' : review_form
            }
            return render(request,'community/form.html', context)
    else:
        return redirect('accounts:login')


@login_required
@require_POST
def delete(request, movie_pk, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.user != request.user:
            return redirect('community:detail', review.pk)
        else:
            if request.method == "POST":
                review = get_object_or_404(Review, pk=review_pk)
                review.delete()
                return redirect('community:review_list', movie_pk)
            else :
                return redirect('community:detail', movie_pk, review.pk)

    else:
        return redirect('accounts:login')


@login_required
def comment_create(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()

        return redirect('community:detail', movie.pk, review.pk)

@require_POST
def comment_delete(request, movie_pk, review_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.is_authenticated:
        if request.method == "POST":
            comment = get_object_or_404(Comment, pk=comment_pk)
            if comment.user == request.user:
                comment.delete()
        return redirect('community:detail', movie.pk, review_pk)
    else :
        return redirect('accounts:login')

def like(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user.is_authenticated :
        if review.like_users.filter(id=request.user.pk).exists():
            review.like_users.remove(request.user)
        else:
            review.like_users.add(request.user)

    else :
        return redirect('accounts:login')

    return redirect('community:detail', movie_pk, review_pk)
```

* models.py

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_url = models.TextField()
    director = models.CharField(max_length=100)
    open_date = models.CharField(max_length=100)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=30)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews", blank=True)

class Comment(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   review = models.ForeignKey(Review, on_delete=models.CASCADE)
   content = models.CharField(max_length=200)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

```

* forms.py

```python
from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title','content','rank']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

```

* admin.py

```python
from django.contrib import admin
from .models import Movie
# Register your models here.
admin.site.register(Movie)
# admin.site.register(Review)
# admin.site.register(Comment)
```

* templates/community/index.html

```html
{% extends 'base.html' %}
{% block body %}

<h2 class="text-center">영화 게시판</h2>

<hr/>

<div class="row row-cols-1 row-cols-md-3">
   {% for movie in movies %}

  <div class="col mb-4">
    <div class="card">
      <img src="{{movie.poster_url}}" class="card-img-top"  style="height: 30rem;">
      <div class="card-body">
        <h5 class="card-title text-center">{{movie.title}}</h5>
         <hr/>
        <p class="card-text">
          <ul class="d-flex flex-column">
            <ul>감독 : {{movie.director}}</ul>
            <ul class="mb-3">개봉일 : {{movie.open_date}}</ul>
          <a href="{% url 'community:review_list' movie.pk %}" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">리뷰작성</a>

             </ul>



        </p>
      </div>
    </div>
  </div>
     {% endfor %}
</div>




{% endblock %}
```

* templates/community/form.html

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block body %}
{% if request.resolver_match.url_name == 'create' %}
<h3>{{movie.title}}영화의 리뷰 쓰기</h3>
<a href="{% url 'community:review_list' movie.pk %}">BACK</a>
<form action="" method="POST">

{% else %}
<h3>{{movie.title}}영화의 리뷰 수정하기</h3>
<a href="{% url 'community:review_list' movie.pk %}">BACK</a>
<form action="" method="POST">
{% endif %}

{%csrf_token%}
{% bootstrap_form review_form %}
<button>SUMBIT</button>
</form>

{% endblock %}
```

* templates/community/review_detail.html

```html
{% extends 'base.html' %}
{% load bootstrap4%}
{% block body %}


<h1 class="text-center my-5">영화 {{movie.title}}</h1>
<div class="d-flex flex-column w-75 mx-auto">
<div class="card border-dark my-3">
    <div class="card-header display-5">
        <ul class="d-flex justify-content-between align-items-center mb-0">
            <h2>제목 : {{review.title}}</h2>
            <p><a href="{% url 'accounts:profile' review.user.username %}">{{review.user.username}}</a>님의 글</p>
        </ul>
    </div>
    <div class="card-body text-dark">
    <h4 class="card-text">{{review.content}}</h4>
    <p class="card-text" style="color:slategrey">
        {% if request.user in review.like_users.all %}

        <a href="{% url 'community:like' movie.pk review.pk %}"><i class="fas fa-kiss-wink-heart" style="color:red"></i></a>

        {% else %}

         <a href="{% url 'community:like' movie.pk review.pk %}"><i class="far fa-kiss" style="color:black"></i></a>
        {% endif %}

         {{review.like_users.all.count }}명이 좋아합니다.
    </p>
      <p class="card-text" style="color:slategrey">Rank: {{review.rank}}</p>

      <p class="card-text" style="color:slategrey">작성 시간: {{review.created_at}}</p>
      <p class="card-text" style="color:slategrey">업데이트 시간: {{review.updated_at}}</p>
    </div>
  </div>
    <div class="d-flex justify-content-center align-items-center ">
    <button><a  class="text-decoration-none" href="{% url 'community:review_list' movie.pk %}" >BACK</a></button>
    {% if review.user == request.user %}
    <button class='mx-3'><a  class="text-decoration-none"  href="{% url 'community:update' movie.pk review.pk %}">수정</a></button>
        <form action="{% url 'community:delete' movie.pk review.pk %}"  method="POST">
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
        <form action="{% url 'community:comment_delete' movie.pk review.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <button>삭제</button>
        </form>
        {% endif %}
        <hr/>
        {% endfor %}
    </div>

    {% if user.is_authenticated %}
    <form action="{% url 'community:comment_create' movie.pk review.pk %}" method="POST">
        {% csrf_token %}
        {% bootstrap_form comment_form %}
        <button>SUBMIT</button>
    </form>
    {% endif %}
    </div>

</div>




{% endblock %}
```

* templates/community/review_list.html

```html
{% extends 'base.html' %}
{% block body %}
<h2 class="text-center">영화 <{{movie.title}}> 리뷰 게시판</h2>
<a class="m-1" href="{% url 'community:create' movie.pk %}">NEW</a>
<a href="{% url 'community:index' %}">BACK</a>

<hr/>
<div>
<table class="table">
    <thead class="thead-dark">
      <tr>
        <th scope="col">#</th>
        <th scope="col">USER</th>
        <th scope="col">RANK</th>
        <th scope="col">TITLE</th>
        <th scope="col">UPDATE</th>
        <th scope="col">DETAIL</th>


      </tr>
    </thead>
    <tbody>
    {% for review in movie.review_set.all %}
      <tr>
        <th scope="row">{{ forloop.counter }}</th>
        <td><a href="{% url 'accounts:profile' review.user.username %}">{{review.user.username}}</a></td>
        <td>{{ review.rank}}</td>
        <td>{{ review.title}} [{{review.comment_set.count}}]</td>
        <td>{{ review.updated_at}}</td>
        <td><a href="{% url 'community:detail' movie.pk review.pk %}">DETAIL</a></td>
      </tr>
    {% endfor %}

    </tbody>
  </table>
  <hr/>
  </div>

{% endblock %}
```

---

### accounts

* urls.py

```python
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/follow/', views.follow, name='follow'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

```



* models.py

```python
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    image = models.ImageField(blank=True)

    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='followings'
        )
```



* forms.py

```python
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','first_name','last_name','email', 'image']
```



* views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def signup(request):
    if request.user.is_authenticated:

        return redirect('community:index')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')

    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/signup.html', context)



def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')

    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)

    return redirect('community:index')

@login_required
def profile(request, username):

    User = get_user_model()
    user = get_object_or_404(User, username=username )

    context={
        'person':user,

    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, username ):
    you = get_object_or_404(get_user_model(), username=username )
    me = request.user

    if you != me :
        if you.followings.filter(pk=me.pk).exists():
            you.followings.remove(me)

        else:
            you.followings.add(me)

    return redirect('accounts:profile', you.username )





```



- templates/accounts/login.html

```html
{% extends 'base.html'%}
{% load bootstrap4 %}
{% block body %}

<div class='m-5'>
<h3>로그인 페이지</h3>
<hr>

<form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}

    <button>로그인</button>
    <button><a class="tect-decoration-none" href="{% url 'community:index'  %}">Back</a></button>
</form>
</div>
{% endblock %}
```

- templates/accounts/profile.html

```html
{% extends 'base.html' %}
{% load static %}
{% block body %}
<h1>{{person.username}}님의 프로필</h1>
<br>
<div class="card" style="width: 18rem;">
    <img class="card-img-top" src="data:image/jpeg;base64,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" alt="Card image cap">
    <div class="card-body">
      <h5 class="card-title">성 : {{person.last_name}}</h5>
      <h5 class="card-title">이름 : {{person.first_name}}</h5>
      <p>email : {{person.email}}</p>
      <br>
      <p class="card-text">
          {{person.followings.count }}명이 팔로우하고 있습니다.
          <br>
        {{person.followers.count }}명을  팔로우하고 있습니다.
      </p>
    {% if user != person %}
        {% if request.user not in person.followings.all %}
       <a href="{% url 'accounts:follow' person.username %}" style="width: 15rem;" class="btn btn-primary">follow</a>
        {% else %}
        <a href="{% url 'accounts:follow' person.username %}" style="width: 15rem;" class="btn btn-primary">unfollow</a>
        <p>당신은 {{person.username}}을 팔로우 하고 있습니다.</p>
        {% endif %}
    {% endif %}

    </div>
  </div>
  <br>
  <a class="text-decoration-none" href="{% url 'community:index' %}" >Home</a>

  <hr/>


  <p>내가 팔로우 하고 있는 사람들 follower</p>
  {%for follower in person.followers.all %}
  <p>{{follower}}</p>
  {%endfor%}
  <hr/>
  <p>나를 팔로우 하고 있는 사람들 followings</p>
  {%for following in person.followings.all %}
  <p>{{following}}</p>
  {%endfor%}

{% endblock %}
```

- templates/accounts/signup.html

```html
{% extends 'base.html'%}
{% load bootstrap4 %}
{% block body %}
<h1>회원 가입</h1>
<hr>
<form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {%bootstrap_form form%}
    <button>
        회원가입
    </button>
    <a href="{% url 'community:index' %}">Back</a>
</form>

{% endblock %}
```
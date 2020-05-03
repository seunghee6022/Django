# 0428 follow  & profile Workshop

* views.py

```python
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
#커스터마이징한 폼
# from .models import Article
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@login_required
def profile(request, username):

    User = get_user_model()
    user = get_object_or_404(User, username=username )
    # articles = Article.user.objects.filter(pk=user.pk).all()
    context={
        'person':user,
        # 'articles':articles,

    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, username ):
    you = get_object_or_404(get_user_model(), username=username )
    me = request.user
    #내가 날 팔로우하지 않기 위함
    if you != me :
        #너를 팔로우 하고있었다면
        if you.followers.filter(pk=me.pk).exists():
            #너의 팔로우에서 나를 지워줘
            you.followings.remove(me)
        #널 팔로우 하지 않고 있었다면
        else:
            #너에 팔로우에 나를 추가해줘
            you.followings.add(me)
    return redirect('accounts:profile', you.username )



```

* models.py

```python
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
```

* forms.py

```python
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','first_name']
```

* profile.html

```html
{% extends 'base.html' %}
{% block content %}
<h1>{{person.username}}님의 프로필</h1>
<h2>이름 : {{person.first_name}}</h2>

{% if user != person %}
    {% if request.user not in person.followings.all %}
    <h3><a href="{% url 'accounts:follow' person.username %}">follow</a></h3>
    {% else %}
    <h3><a href="{% url 'accounts:follow' person.username %}">unfollow</a></h3>
    <p>당신은 {{person.username}}을 팔로우 하고 있습니다.</p>
    {% endif %}
{% endif %}
<hr/>
<h3>{{person.followings.count }}명이 팔로우하고 있습니다.</h3>
<h3>{{person.followers.count }}명을  팔로우하고 있습니다.</h3>

<hr/>
<h3>{{person.username}}님이 작성한 글들</h3>
<ul>
{% for article in articles %}

<li>{{article.title}}</li>

{% endfor %}
</ul>
{% endblock %}
```

---

### 결과 사진

* index.html

![](C:\Users\tgb03\Desktop\online-lecture\0428\workshop\index.PNG)

* profile.html
  * 본인의 페이지 접속 시

![](C:\Users\tgb03\Desktop\online-lecture\0428\workshop\본인 페이지.PNG)

* 다른 사람 페이지 접속 시

![](C:\Users\tgb03\Desktop\online-lecture\0428\workshop\다른회원 페이지.PNG)
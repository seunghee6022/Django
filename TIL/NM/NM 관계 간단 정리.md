# N:M 관계 간단 정리/ 좋아요 기능

* N:M - > 중개 테이블 필요

![](C:\Users\tgb03\Desktop\online-lecture\0428\N대M.PNG)

![](C:\Users\tgb03\Desktop\online-lecture\0428\중개 테이블 필요.PNG)

* GS가 마신 주류 목록 알고싶으면?

1. 중개테이블 이용

```python
#GS가 1명만 있다는 전제하에 filter말고 그냥 get씀.
GS = 참석자.get(이름='GS')
GS.판매_set.all()
```

2. ManyToManyField이용

```python
class 참석자:
    참석자명

class 주류:
	주류명 = 정의정의...
    people = ManyToManyField(참석자(어떤 테이블과 N:M관계할지-> 하고나서 바로 주류테이블에 참석자_id column생김), related_name="주류들")
    
class 판매:
    참석자
    주류
    
```



```python
# ManyToMany로 바로 참석자 column통해 바로 접근 가능
새벽이슬.people.all()

# 설정 안해서 원래 방식대로 set으로 접근해야
참석자.주류_set.all()

#만약 realated_name="주류들"로 설정했을시에는 더이상 
참석자.주류_set.all() - (x) 못함,
참석자.주류들.all() - (o) 만 가능
```

---

### 좋아요 기능

* articles/models.py

```python
from django.db import models
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    #글 작성자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 좋아요 누른 사용자
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles", blank=True)
```

* N:M 접근 방식(중요)

```python
# article = Article.objects.get(?)으로 특정 게시물을 가져온 상태에서 가정

article.user : 게시글을 작성한 유저
article.like_users.all(): 게시글을 좋아요 누른 유저들(직접 참조)
user.article_set.all() : 유저가 작성한 게시글들(역참조)
user.like_articles.all() : 유저가 좋아요 누른 게시글들(related_name으로 역참조.)
------------------------- 수업 Quiz -----------------------------
* 로그인 한 유저가 작성한 모든 게시글 목록 정보
1.Article.objects.filter(user = request.user)
#로그인한 유저
2.user = request.user
user.article_set.all()

* 로그인한 유저가 누른 좋아요 게시글 목록 정보
user.likes_articles.all()
# related_name이 없을 때
user.
```

* 관계와 역참조 설명 

![](C:\Users\tgb03\Desktop\online-lecture\0428\관계와 역참조.PNG)



* urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/like/', views.like, name="like"),
]
```

* forms.py

```python
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        #'like_users'추가
        exclude = ['created_at', 'updated_at', 'user','like_users']
```

* views.py

```python
# 좋아요 로직 구현 (2가지 경우 생각)
# 1. 좋아요가 눌리지 않은 경우
# 2. 좋아요가 이미 눌려져 있는 경우
```

```python

# 로그인한 유저만 보여줘야
# @login_required를 is_authenticated대신 사용해도 됌
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.user.is_authenticated :
    #좋아요가 눌리지 않은 경우
        if request.user not in article.like_users.all():
        # 같은 표현 : if article.lick_users.filter(id=request.user.pk).exists():
            article.like_users.add(request.user)

        #좋아요가 이미 눌려져 있는 경우
        else:
            article.like_users.remove(request.user)
    else :
        return redirect('accounts:login')

    return redirect('articles:index')
```

* login_required - 자동으로 로그인 페이지로 돌려줌. next로 다시 이동하게 만들 수 없다.
* `request.user.is_authenticated()` vs `@login_required`









* index.html

```html
{% extends 'base.html' %}

{% block content %}
  <h2>INDEX</h2>
  <a href="{% url 'articles:create' %}">NEW</a>
  {% for article in articles %}
    <ul>
      <li>{{ article.user }}의 {{ article.pk }}번글</li>
      <li>제목: {{ article.title }}</li>
      <li>내용: {{ article.content }}</li>
      {% if request.user in article.like_users.all %}
      <li><a href="{% url 'articles:like' article.pk %}"><i class="far fa-kiss"></i></a></li>
      {% else %}
      <li><a href="{% url 'articles:like' article.pk %}"><i class="fas fa-kiss-wink-heart"></i></a></li>
      {% endif %}
    </ul>
    <hr>
  {% endfor %}
{% endblock %}
```





----

### 팔로우 (User <-> User)

* models.py

```python
from django.conf import settings
from django.contrib.auth.models import AbstractUser
#User를 참조하므로 settings.AUTH....를 첫번째 인자로 넣음
class User(AbstractUser):
    followers = 
    models.ManyToManyField(settings.AUTH_USER_MODEL,
                     related_name ='followings')
    
    
# custom user설정할 떄는 안에 내용이 없어도
'''
class User(AbstractUser):
    pass
    
라도 하는걸 권장    
'''

```



* settings.py

```python
#custom user모델로 대체하기 위해서는 유저모델 이름 다시 정해야 `myapp_user`로

# default = 'auth_user'
AUTH_USER_MODEL = 'accounts.User' 추가

```



* admin.py

```python
from django.contrib import admin
from .models import User

admin.site.register(User)
```



* forms.py (커스텀 유저를 사용하면 반드시 커스텀 폼도 만들어야)

```python
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        #클래스를 넣어줘야하기 때문에 get_user_model()함수를 넣어준다.
        fields = ['username','first_name','last_name','email']
        
        
clas CustomCreationForm(USerCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email','username']
```

* views.py (기존에 사용하던 폼들 모두 커스텀폼으로 이름 바꿔야)

```python
import 하고 다 바꿔주기
```



* 왜 로그인은 커스텀으로 바꿨는데도 잘 작동하는가?

정답 : 모델폼이 아니라서 forms.Form을 상속받고 있기 때문에

---

### 팔로우 기능 본격 구현 (accounts app내)

![](C:\Users\tgb03\Desktop\online-lecture\0428\팔로우 기능 컨셉.PNG)

* urls.py

```python
path('<int:pk>/follow/', views.follow, name='follow'),
```



* views.py (좋아요와 거의 기능이 유사하다)

```python
def follow(request, pk):
    #User클래스 활용위해서 가져와야
    User = get_user_model() 
    #팔로우 당하는 사람
    user = get_object_or_404(User, pk=pk)
    #팔로우 요청한 사람 -> request.user
    
    # 자기스스로 팔로우 막기 위해
    if user != request.user :
        #팔로우가 되어있따면 
        if user.followers.filter(pk=request.user.pk).exist():
            #삭제
            user.folloers.remove(request.user)
        #아니면
        else :
            #추가
            user.followers.add(request.user)
    return redirect('accounts:detail', user.pk)
    
```



* detail.html (내가 몇명 팔로우하고 몇명이 나를 팔로우 하는지 확인)

1. count사용

```html

{%if request.user in user.follow.all %}
<a href="{% url 'accounts:follow' user.pk %}">팔로우 취소</a>
{% else %}
<a href="{% url 'accounts:follow' user.pk %}">팔로우 취소</a>
{% endif %}
<p> {{user.followers.count }} 명이 팔로우 하고 있습니다.</p>

```

2. with 사용해서 count

```html
{% with user_followers = user.followers.all %}
{%if request.user in user.follow.all %}
{% if request.user in user_followers %}
<a href="{% url 'accounts:follow' user.pk %}">팔로우 취소</a>
{% else %}
<a href="{% url 'accounts:follow' user.pk %}">팔로우 취소</a>
{% endif %}
#팔로우 당하는 사람 -> user
<p> {{user_followers|length }} 명이 팔로우 하고 있습니다.</p>

```

3. 최종

```html
...
```



* 현재 column명 -->  __from_user_id,  to_user_id__

좋아요(Article <-> User : article_id, user_id)

팔로우(User <-> User : from_user_id,  to_user_id)

---

 ### 팔로우 zoom 복습

* User customizing 하면 회원가입시 auth.user 에러 뜸

->UserCreationForm은 auth.user를 사용하기 때문에 form을 커스터마이징해야

---

* _ 변수
* . 클래스
# 0428 좋아요 기능 구현 exercise

* views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)

# 로그인한 유저만 보여줘야
# @login_required
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

* models.py

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
    # 좋아요 한 사람들 - 게시글에서는 좋아요 한 사람들을 직접 참조 가능하고,
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles", blank=True)
```

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
      <li><a href="{% url 'articles:like' article.pk %}"><i class="fas fa-kiss-wink-heart" style="color:red"></i></a></li>

      {% else %}
       <li><a href="{% url 'articles:like' article.pk %}"><i class="far fa-kiss" style="color:black"></i></a></li>
      {% endif %}
      <li>{{article.like_users.all.count }}명이 좋아합니다.</li>
    </ul>
    <hr>
  {% endfor %}
{% endblock %}
```

---

* 결과 사진

![](C:\Users\tgb03\Desktop\online-lecture\0428\exercise\결과사진.PNG)
# 0407 CRUD with ModelForm workshop

* articles/urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [   
    path('', views.index, name= 'index'),
    path('new/', views.new, name= 'new'),
    path('<int:pk>/', views.detail, name= "detail"),
    path('<int:pk>/update/', views.update, name= 'update'),
    path('<int:pk>/delete/', views.delete, name= 'delete'),
    
]
```

* articles/views.py

```python
from django.shortcuts import render,redirect,get_object_or_404
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # -pk하면 내림차순으로 정렬
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.order_by('pk')
    context = {
        'articles':articles
    }
    return render(request,'articles/index.html', context)

def new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        #검증하기
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')

    else :
        #GET
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/new.html',context)

def detail(request,pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html',context)

def update(request,pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        
        form = ArticleForm(request.POST, instance=article)
        #검증하기
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)

    else :
        #GET
        form = ArticleForm(instance = article)
    context = {
        'form': form,
        'article': article
    }
    return render(request, 'articles/update.html', context)

def delete(request,pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')


```



* articles/update.html

```html
{% extends 'base.html'%}
{% block content %}
    <h2>EDIT</h2>
    <form action="" method="POST">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="submit">
    </form>
    <a href="{% url 'articles:detail' article.pk %}">BACK</a>


{% endblock %}
```

![](C:\Users\tgb03\Desktop\online-lecture\0407\workshop\update.PNG)
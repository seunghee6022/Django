# 0421 Comment function Workshop

1. Model

   * models.py

   ```python
   from django.db import models
   from django.conf import settings
   
   class Article(models.Model):
       title = models.CharField(max_length=100)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   
   
   class Comment(models.Model):
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       article = models.ForeignKey(Article, on_delete=models.CASCADE)
   
   ```

   * forms.py

   ```python
   from django import forms
   from .models import Article,Comment
   
   class ArticleForm(forms.ModelForm):
       class Meta:
           model = Article
           fields = '__all__'
   
   class CommentForm(forms.ModelForm):
       class Meta:
           model = Comment
           fields= ['content']
   ```

2.  Comment Create

   * urls.py

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'articles'
   
   urlpatterns = [
       path('', views.index, name='index'),
       path('<int:article_pk>/', views.detail, name='detail'),
       path('create/', views.create, name='create'),
       path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
       path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name= "comment_delete"),
   ]
   ```

   * views.py

   ```python
   from .models import Article, Comment
   from .forms import ArticleForm, CommentForm
   
   # GET요청 : 댓글 작성할 수 있는 Form 반환
   def detail(request, article_pk):
       article = get_object_or_404(Article, pk=article_pk)
       comment_form = CommentForm()
       context = {
           'article': article,
           'comment_form' : comment_form,
       }
       return render(request, 'articles/detail.html', context)
   
   # POST요청 : 사용자가 입력한 댓글을 검사하고 DB에 저장한다.
   def comments_create(request,article_pk):
       article = get_object_or_404(Article, pk = article_pk)
       comment_form = CommentForm(request.POST)
       if comment_form.is_valid(): #댓글 검사
           comment = comment_form.save(commit = False)
           comment.article = article
           comment.save()#DB에 저장
           return redirect('articles:detail', article.pk)
   ```

   

3. Comment Read

   * detail.html

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
   	<h2>DETAIL</h2>
   	<hr>
   	<h3>{{ article.pk }}번글</h3>
   	<p>제목: {{ article.title }}</p>
   	<p>내용: {{ article.content }}</p>
   	<p>생성 시각: {{ article.created_at }}</p>
   	<p>수정 시각: {{ article.updated_at }}</p>
   	<a href="{% url 'articles:index' %}">BACK</a>
   
   	<h3>댓글 작성</h3>
   	<ul>
   	{% for com in article.comment_set.all %}
   	<li>
   		{{com.content}}
   		<form action="{% url 'articles:comment_delete' article.pk com.pk %}" method="POST">
   			{% csrf_token %}
   			<button>삭제</button>
   		</form>
   	</li>
   	{% endfor %}
   	</ul>
   
   	<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
   		{% csrf_token %}
   		{{comment_form.as_p}}
   		<button>보내기</button>
   	</form>
   
   {% endblock %}
   ```

4. Comment Delete

   * views.py

   ```python
   def comment_delete(request, article_pk, comment_pk):
       if request.method == "POST":
           comment = get_object_or_404(Comment, pk=comment_pk)
           comment.delete()
           #되돌아가는곳의 정보로 article_pk사용
       return redirect('articles:detail', article_pk)
   ```

---

### 결과 사진

* 댓글 달기

![](C:\Users\tgb03\Desktop\online-lecture\0421\workshop\댓글 삭제 전.PNG)

* 댓글 삭제 후

![](C:\Users\tgb03\Desktop\online-lecture\0421\workshop\삭제 후.PNG)
# 0421 SQL Live 강의

---

### orm vs sql 복습

#### 쿼리(메서드)

* 조회(lookup)
  * get -> 쿼리 결과가 오직하나여야, 나머지는 모두 에러(0개, 여러개 모두 오류 반환)
    * 주로 article RUD할 때 무조건 하나여야
  * filter -> 무조건 Queryset반환
    * 정확하게 찾고 싶을 때
      * AND -> 메서드 체이닝 e.g. .filter.filter, 키워드 인자로 여러개 넘겨줌
      * OR -> 위 방법으로 못함, 그래서 Q로 묶어서 표현
    * 같을 때 , 일치할 때 -> 키워드 인자로 가능 =
    * < , >, <=. >=  -> 키워드 인자 불가능 __gt/lt/gte/lte
  * 상황마다 에러를 발생/ 어떤 값을 던져줌 다름 그때 get/filter 구분해서 사용
  * e.g. dict에서 value를 가져오는 것은 동일한데
  * ''이름'' key가 없으면 keyError를 발생시킴
  * 그러나 dict.get('이름') ->None 반환

* Q (OR)

> orm의 Q = sql의 OR

```sql
#orm
from django.db.models import Q
User.objects.filter(age= 30, last_name='김').count()
#위처럼 키워드 인자로 or 넘기는게 불가능하므로 Q를 사용
User.objects.filter(Q(age=30) | Q(last_name='김')).count()
```

```sql
#sql
SELECT COUNT(*) FROM info
WHERE age = 30 OR last_name = '김';
```



### 표현식

`aggregate` 메서드 사용

> 개별 object CRUD를 django쿼리를 통해 가능.
>
> 만약 collectoin of objects == Queryset의 요약된 정보를 얻고 싶으면, aggregate 메서드를 써야 한다.



### Group by

`annotate` 메서드 사용

> 주석달기 느낌 특정값 붙이고 싶을 때 e.g. 게시물들에 대해 댓글 수 같이 표시
>
> 1 : N 



---

---



## Django project class --> table

* 회원/ 로그인/로그아웃 User-->  auth_user(table)
* 게시글  Article --> articles_article(table)



### Foreign Key (1 : N - > N인 곳에 1을 FK로 추가)

> user  <---------> artices_article
>
> 게시판에서 
>
> 1. user에 글번호들을 저장
> 2. 글번호에 user를 저장
> 3. 둘다
>
> 정답 ) 2번

해설 ) 유저 한명 : 여러개 게시글 = 1 : N

​		--> 유저 하나에 N개의 article 을 넣을 수 없다. 원자성 위배

​		__N개의 게시글 테이블에 FK(Foreign key)추가해서  속성 1개만 추가시킨다.__

---

### 기본 쿼리

---

#### 0. 준비

```python
Reporter.objects.create(username='요트맨')
Reporter.objects.create(username='John')
Reporter.objects.create(username='Justin')
Reporter.objects.create(username='Neo')

# r1 = 요트맨
r1 = Reporter.objects.get(pk=1)
```

#### 1. article 생성

```python
a1 = Article()
a1.title = '제목1'
a1.content = '내용1'
#reporter는 리포터 오브젝트를 저장
a1.reporter = r1
#reporter_id는 숫자(INTEGER)를 저장
#a1.reporter_id = 1
a1.save()
```

```python
#a2(게시글2)도 r1(리포터1)=요트맨이 작성한 것
a2 = Article.objects.create(title='제목2', content='내용2', reporter=r1)
```



#### 1:N 관계 활용

```python
#1.글의 작성자
a2 = Article.objects.get(pk=2)
a2.reporter

#2.글의 작성자의 username
a2.reporter.username

#3.글의 작성자의 id
a2.reporter.id
a2.reporter_id
#둘 다르다 . 값은 같을지언정 

#4.작성자의 글 -> article 오브젝트가 반환되는게 핵심
r1 = Reporter.objects.get(pk=1)
r1.article_set.all()
#=> <QuerySet [.....]

#5.1번 글의 작성자가 쓴 모든 글
a1 = Article.objects.get(pk=1)
a1.reporter.article_set.all() #-->결과는 QuerySet
```





### 1 : N

```python
#1
class Reporter(models.Model):
    username = models.CharField(max_length=10)
    
#N
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    #FK이름 지을 때 해당 모델명(Reporter)의 소문자 이름(reporter)으로 짓자 
    reporter =  models.ForeignKey(Reporter, on_delete=models.CASCADE)
    #나중에 reporter뒤에 _id가 붙어서 Article의 column에 저장된다. -> reporter_id
    # cf. reporter_id로 선언하지 않게 조심 -> 그럼 Article column에는 reporter_id_id로 저장됨
```

* `articles_article`테이블에 `reporter_id'컬럼이 추가 된다.
* `reporter`의 경우 `article_set`으로 N개(QuerySet)를 가져올 수 있다.
* `article`의 경우 `reporter`로 1에 해당하는 오브젝트를 가져올 수 있다.
* `on-delete` : 참조 대상이 삭제되는 경우
  * `CASCADE` : 해당 객체(`reporter`)가 삭제 되었을 때 참조하는 객체(`articles`)도 모두 삭제
  * `protect` : 참조하는 객체가 존재하면 삭제 금지
  * `SET_NULL` : NULL 값으로 치환. NOT NULL 옵션이 있는 경우는 활용할 수 없음
  * `SET_DEFAULT` : 디폴트 값(`article`)을 참조하게 끔 한다.



---



### 참고용 교수님 코드 전체적 흐름 따라 친 것

```python
Reporter.objects.create(username='요트맨')
Reporter.objects.create(username='John')
Reporter.objects.create(username='Justin')
Reporter.objects.create(username='Neo')

Reporter.objects.all()

r1 = Reporter.objects.get(pk=1)
#r1.username 확인용
article = Article()
article.title = '제목1'
article.content = '내용1'

#FK 등록
article.reporter = r1

article.reporter
article.reporter.id
-->1
article.reporter.username
-->요트맨

#sql table로도 확인가능

a2 = Article.objects.create(title='제목2', content='내용2', reporter_id=2)
#저장 확인용
a2
a2.reporter
a2.reporter.username
a2.reporter_id
```

```python
r2 = Reporter.objects.get(pk=1)
r2.username 
Article.objects.filter(reporter_id=2)
#r2가 위의 정보를 한번에 가지고 오고 싶을 때
#특정 object로 부터 가져오게 함
r2.article_set.all()

#둘 다 똑같은 Queryset을 프린트함
print(r2.article_set.all().query)
print(Article.objects.filter(reporter_id=2).query)

r3 = Reporter.objects.get(pk=3)
r3.article_set.all() --> Queryset이 담겨져 있다

```



---

---



### Django 



* models.py

```python
from django.conf import settings #추가

class Article(models.Model):
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #추가
```



* 마이그레이션

```python
python manage.py makemigrations
python manage.py migrate
```

-> structure) column에  user_id 생김. -> 사용할 준비 ok



* 글쓰기 Form에서 user_id가 같이 입력되도록 뜨므로 forms.py에 fields를 사용자 지정으로 바꾼다.

```python
#forms.py

class ArticleForm(...)
	...
    fields = ['title','content']로
```



* 글쓰고 작성할 때 user(user_id)에 작성자의 id 넣어주기(user_id의 무결성 법칙에 위배되므로 views.py에서 __user_id를 NOT NULL__로 해줘야 됨)
  * create 저장 로직에서 request.user의 id값을 저장해줘야한다.
  * model에서 commit(SQL 쿼리로 db에 날려버림)하기 전에 저장을 안하게 해야 NOT NULL 조건을 넣을 수 있다. `commit=false` 사용
  * 그 다음 저장 못하게 막아두고 user 왜래키(user_id)에 기존의 작성자의 id값을 넣어준다(NOT NULL해결)
  * 그러고 save한다.

```python
def create(request):
    ...
    if form.is_valid():
        #설명 위에
        article = form.save(commit=false)
        article.user = request.user
        article.save()
        return redirect ('articles:index')
    ...
```



* article.user VS article.user.username
  * article.user => User class의 instance != article.user.username ( User class를 실행할 때 username이 출력되도록만 한거라 보이는 것만 똑같지 다르다. 그냥 print한 결과가 username이랑 같은...)
  * article.user.username => 해당 instance의 user의 username. 출력 형태 : String문자열 형태



* 현재 작성자가 아니라도 작성된 글을 수정.삭제할 수 있다.

`{% if article.user == request.user %}` 로` 작성자==사용자` 검사

```html
#detail.html

#작성자 == 사용자
{% if article.user == request.user %}
<form action="{% url ....%}"...>
    
</form>
{% endif %}
```

```python
#views.py

@require_POST
@login_required
def delete(request,pk):
    article = get_object_or_404(Article,pk=pk)
    if request.user == article.user:
        article.delete()
        return redirect('articles:index')

@login_required
def update(request,pk):
    article =
    if request.method=='POST':
        form = 
        if form.is_valid():
            article = ..
            if article.user == request.user:
                article.save()
                return redirect ...
        else :
            form = ...
        context = {
            ...
        }
        return render()
   	else :
        rethrn redirect('articles:index')
                
```



### 1:N ( article comment 댓글 기능 추가)

>작성창 - detail.html에
>
>처리는 views.py에서

1. model 만들기

```python
#models.py
from django.conf import settings #추가

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

models.py 수정 후에  --> `python manage.py migrate` 하기



2. 댓글 작성 창 만들기 -->`detail.html`

```html
#detail.html 
...
#댓글 폼으로 만들기
<h3>댓글</h3>
{% for comment in article.comment_set.all %}
	<li>{{comment.user.username}}:{{comment.content}}</li>
{% endfor %}
<hr/>
<form action="{% url 'article:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <button class="btn btn-primary">
        작성
    </button>
</form>

```

3. 댓글창 모델 폼으로 만들기

```python
# forms.py
class CommentForm(forms.ModelForm):
    class Meta
    model = Comment
    fields = ['content']
```

4. views.py에 def detail에 댓글 넘기기 추가

```python
from django.contrib.auth.forms import CommentForm

def detail(request, pk):
    article = 
    form = CommentForm() #추가
    context = {
        'article':article,
        'form':form
    }
    return ..   
```

5. urls.py에 path추가

```python
path('<int:pk>/comments/', views.comment_create, name='comments_create')
```

6. forms.html

```html
<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
</form>
```

7. views.py에 def comment_create

```python
from django.contrib.auth.forms import CommentForm

@login_required
@require_POST
def comments_create(request,article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            return redirect('articles:detail', articles.pk)
    
```

```python

```


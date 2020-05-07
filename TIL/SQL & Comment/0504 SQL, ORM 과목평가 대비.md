# 0504 과목평가 대비

1. SQL
   * 명령어
   * 키워드 사용법
   * 이름
2. Django ORM(모델 선언 방법, 활용방법 중심)
   * CRUD
   * 1:N
   * N:M

---

### 1. SQL(Structured Query Language)

* 명령어

  * DDL(Data Definition Language) - `CREATE`, `ALTER`, `DROP`

  

  * DML(Data Manipulation Language) - `INSERT`,`SELECT`,`UPDATE`,`DELETE`
  * DCL(Data Control Language) - `BEGIN`,`COMMIT`

* 키워드 사용법 (0421 Exersize 참고)

  * 나이가 30살 이상인 사람의 인원 수

  ```python
  #orm
  User.objects.filter(age__gte=30).count()
  #sql
  SELECT COUNT (*) FROM
  WHERE age >= 30 ;
  ```

  * 나이가 30이면서 성이 김씨인 사람의 인원수

  ```python
  #orm
  User.objects.filter(age=30, last_name='김').count()
  #sql
  SELECT COUNT (*) FROM users_user
  WHERE age=30 and last_name='김';
  ```

  * 나이가 30이거나 성이 김씨인 사람의 인원수 (or -> Q사용)

  ```python
  from django.db.models import Q
  #orm
  User.objects.filter(Q(age=30)|Q(last_name='김')).count()
  #sql
  SELECT COUNT(*) FORM users_user
  WHERE age=30 or last_name='김';
  ```

  * 지역번호가 02로 시작하는 사람의 인원수

  ```python
  #orm
  User.objects.filter(phone__startswith='02-').count()
  #sql
  SELECT COUNT (*) FROM users_user
  WHERE phone LIKE '02%';
  ```

  * phone에 123포함하고 age가 30 미만인 사람 정보 조회

  ```python
  #orm
  User.objects.filter(phone__contains='123',age__lt=30).values()
  #sql
  select * from users_user
  where phone '%123%' like and age < 30 ;
  ```

  ---

  #### 정렬 및 LIMIT, OFFSET

  * 나이가 많은 사람 10명

  ```python
  #orm
  User.objects.order_by('-age')[:10]
  #sql
  SELECT * FROM users_user
  ORDER BY age DESC
  LIMIT 10;
  ```

  * 잔액이 적은 사람 10명

  ```python
  #orm
  User.objects.order_by('balance')[:10]
  #sql
  SELECT * FROM users_user
  ORDER BY balance ASC
  LIMIT 10;
  ```

  * 성, 이름 내림차순 순으로 5번째 있는 사람

  ```python
  #orm
  User.objects.order_by(-'last_name',-'first_name')[4]
  #sql
  SELECT * FROM users_user
  ORDER BY last_name DESC first_name DESC
  LIMIT 1 OFFSET 4;
  ```

  ---

  #### 표현식 `aggregate`

  * 전체 평균 나이

  ```python
  #orm
  User.objects.aggregate(Avg('age'))
  #sql
  SELECT AVG(age) FROM users_user;
  ```

  * 김씨의 평균 나이

  ```python
  #orm
  User.objects.filter(last_name='김').aggregate(Avg('age'))
  #sql
  SELECT AVG(avg) FROM users_user
  WHERE last_name = '김'
  ```

  * 계좌 잔액 중 가장 높은 금액

  ```python
  #orm
  User.objects.aggregate(Max('balance'))
  #sql
  SELECT MAX(balance) FROM users_user;
  ```

  * 계좌 잔액 총액

  ```python
  #orm
  User.objects.aggregate(Sum('balance'))
  #sql
  SELECT SUM(balance) FROM users_user;
  ```

  ---

  #### Group by `annotate` -> 1 : N

  * 지역별 인원 수

  ```python
  #orm
  User.objects.values('country').annotate(Count('country'))
  #sql
  SELECT country, COUNT(country) FROM users_user
  GROUP BY country;
  ```

  ---

  #### Update 값 수정, 변경

  * 이름이 '김옥자'인 사람의 행정구역을 경기도로 수정하시오.

  ```python
  #orm
  1. filter로 불러와서 update하기
  User.objects.filter(first_name='옥자', last_name='김').update(country='경기도')
  2. for문 사용
  users = User.objects.filter(first_name='옥자', last_name='김')
  for user in users:
      user.country = '경기도'
      user.save()
  
  #sql
  UPDATE users_user SET country='경기도'
  WHERE first_name='옥자' AND last_name='김';
  
  ```

  ---

  #### DELETE 삭제

  * 이름이 '백진호'인 사람을 삭제하시오

  ```python
  #orm
  User.objects.filter(last_name='백',first_name='진호').delete()
  #sql
  DELETE FROM users_user
  WHERE last_name='백' AND first_name='진호';
  ```

  ----

  #### DISTINCT 중복 없이

  * phone이 '010'으로 시작하는 사람들의 행정 구역을 중복 없이 조회하시오.

  ```python
  #orm
  User.objects.filter(phone__startswith='010').values('country').distinct()
  #sql
  SELECT country FROM users_user
  WHERE phone='010-%'; ??????distinct어떻게 하지???????
  ```

  ---

  * 제주 특별 자치도에서 사는 사람 중 balance가 가장 많은 사람의 first_name

  ```python
  #orm
  User.objects.filter(country='제주특별자치도').order_by(-'balance')[0].first_name
  ```

---

### 1 : N

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



---

### N : M

---

#### SQL

```sql
-- users_user
CREATE TABLE "users_user" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "first_name" varchar(10) NOT NULL,
    "last_name" varchar(10) NOT NULL,
    "age" integer NOT NULL,
    "country" varchar(10) NOT NULL,
    "phone" varchar(15) NOT NULL,
    "balance" integer NOT NULL
);
-- .read users_user.sql

```

---

#### ORM

1. 좋아요

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

* forms.py

```python
x
```



2. 팔로우

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


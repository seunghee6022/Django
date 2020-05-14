# 0511 Django REST Framework

##  오늘 요점 : Django에서 JSON형식에 맞춰서 DATA만 제공한다.

### Why JSON? 데이터 양이 = 길이가 짧다. 시간 지날수록 데이터 적게쌓임, 시간 절약 -> 돈 아낌

---

![](C:\Users\tgb03\Desktop\TIL\Django REST Framework\Vue.PNG)

* dummy data만드는 함수

```python
#models.py
from faker import Faker

#초기화
f = Faker()

@classmethod
def dummy(cls,n):
    for _ in range(n):
        cls(Article).objects.create(
        title = f.name(),
        content = f.text()
        )
```

```python
ctrl+d 쉘끄기

$python manage.py shell_plus

Article.dummy(10) # 시간 많이 걸리니까 10개미만..

```

---

* views.py

한방에 하는 방법. 다음에 쓸 일 없다. 그냥 보여주기..

```python
from django.http.response import JsonResponse
#django core serializer
@require_GET
def article_list_json_2(request):
    from django.core import serializers
    articles = Article.objects.all()
    data = serializers.serialize('json',articles)
  	return HttpResponse(data,content_type='application/json')
#결과를 스트링으로 만들어줌
    
    
```

### drf(djangorestframework) -> 오늘 내용

```python
$ pip install djangorestframework
```

* settings.py

```python
INSTALLED_APPS = [
    'rest_framework'
]
```



```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ArticleSerializer

#rest framework
@api_view(['GET']) #어떤 요청을 받겠다는걸 지정해줄 수 있다.
def article_list_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)#Many=True를 없애면 값1개만 = 단일객체(단일 모델)만 들어가있을거라 가정. 하지만 articles는 queryset이기 때문에 오류가 난다.
    #rest_Framework의 serializer를 리턴하려면Response
    return Response(serializer.data)
    
```

* urls.py

```python

url_patterns = [
    path('json2/',views.article_list_json_2),
    path('json3/',views.article_list_json_3),
    
]
```

* serializers.py

```python
from rest_ranmework import serializers
from .models import Article

class ArticleSerializer(serializer.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__' #아님 내가 원하는거만 골라올 수 있다.
```

---

### ZOOM



### API(Application Programming Interface)

>  응용 프로그램에서 사용할 수 있도록 운영체제나 프로그래밍언어가 제공하는 기능을 제어할 수 있게 하는 interface(어떤 프로그램과 프로그램 연결해서 제어할 수 있게 해주는..)

예전에는 xml형식. 요새는 JSON(java script ...)



### rest_framwork의 serialiser를 사용하면

원하는 데이터만 json형태로 변환을 해서 가져올 수 있다.



* models.py

```python
from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```



### faker : dummy 데이터 만들기

`pip install faker`

`.bulk_create()` : 1000배 빨리 만들어줌 ->  list comprehension할 수 있다 : 힌트

* musics/models.py

```python
from django.db import models

from faker import Faker

f = Faker()
# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @classmethod
    def dummy(cls,num):
        for _ in range(num):
            cls.objects.create(name=f.name())



class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @classmethod
    def dummy(cls,num):
        for _ in range(num):
            cls.objects.create(
                title=f.text(),
                artist_id=1
                )

class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @classmethod
    def dummy(cls,num):
        for _ in range(num):
            cls.objects.create(
                content=f.text(),
                music_id=random.choice(range(1,5))
                )
```

* api/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1',include('musics.urls')),
]

```



---



* views.py

`@api_view(['GET'])` :반드시 붙여줘야. 아니면 동작 x

```python
from django.shortcuts import render
from .serializers import ArtistSerializer, MusicSerializer
from .models import Artist, Music
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    # form = ArtistForm()과 유사한 형태
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer =MusicSerializer(mucisc, many=True)
    return Response(serializer.data)
```

### 파이썬 shell_plus

`pip install django-extentions`

* settings.py

```python
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'musics',
    'rest_framework',
]

...
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

```

`$ python manage.py shell_plus`

```bash
Artist.dummy(5)
Music.dummy(5)
```

---



* serializers.py

```python
from rest_framework import serializers

from .models import Artist, Music, Comment

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id','title']

class ArtistDetailSerializer(serializers.ModelSerializer):
    #변수처럼 사용할 수 있게 선언해줌
    musics_count = serializers.SerializerMethodField()
    class Meta:
        model = Artist
        fields = ['id','name','musics_count',]
    #get_<field_name>으로 함수이름 정함. obj에 article정보가 들어가있음.
    def get_musics_count(self,obj):
        return f'{obj.music_set.count()}곡'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class MusicDetailSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()
    #소스가 없으면 (뷰에서 들어오는 뮤직을 기반으로 내용을 만듬! )
    # 해결방법1 :어떤 정보 기반으로 할지 소스 정해줘야
    comments = CommentSerializer(source='comment_set',many=True)
    # 해결방법2 : related_name 설정, 변수이름과 동일하게 comments로 맞춰줘야
    # comments = CommentSerializer(related_name='comments',many=True)


    class Meta:
        model = Music
        fields = '__all__'

    def get_comments_count(self,obj):
        return f'{obj.comment_set.count()}개'


```

`serializers.SerializerMethodField()` : 변수처럼 사용할 수 있게

```python
class ArtistDetailSerializer(serializers.ModelSerializer):
    #변수처럼 사용할 수 있게 선언해줌
    musics_count = serializers.SerializerMethodField()
    class Meta:
        model = Artist
        fields = ['id','name','musics_count',]
    #get_<field_name>으로 함수이름 정함. obj에 article정보가 들어가있음.
    def get_musics_count(self,obj):
        return f'{obj.music_set.count()}곡'
```

`

```python

```







* musics/urls.py

```python
from django.urls import path
from . import views
app_name = 'musics'

urlpatterns = [
    path('/artists/',views.artist_list, name='artist_list'),
    path('/musics/',views.music_list, name='music_list'),

]
```

* admin.py

```python
from django.contrib import admin
from .models import Artist,Music,Comment

admin.site.register(Artist)
admin.site.register(Music)
admin.site.register(Comment)


```





---

### LIVE2

```bash
#board에 이미 Article이 있어서 등록이 안되어버림. 따로 등록해줌 -> namespace의 중요성
from blog.models import Article
Article.dummy(10)
```



### serializer 용도별



![](C:\Users\tgb03\Desktop\TIL\Django REST Framework\serializer용도구별.PNG)

### 기존 사용자 고려 방식

![](C:\Users\tgb03\Desktop\TIL\Django REST Framework\기존 방식.PNG)



### 개발자 입장의 방식

![](C:\Users\tgb03\Desktop\TIL\Django REST Framework\개발자의 입장에서 방식.PNG)

detail

![](C:\Users\tgb03\Desktop\TIL\Django REST Framework\개발자입장_detail.PNG)



### 개발자를 위한 데이터 요청과 체크는 어떻게?

![](C:\Users\tgb03\Desktop\TIL\Django REST Framework\개발자는 데이터요청 어떻게.PNG)

> 이전에는 form = ArticleForm(request.POST)사용했는데 이제는 안쓰면 어떻게 데이터를 꺼내고(개발자입장), 사용자는 어떻게 데이터를 보내나=요청하나(사용자입장)????

![](C:\Users\tgb03\Desktop\TIL\Django REST Framework\데이터 처리 어떻게.PNG)

 ### => POSTMAN 포스트맨사용

* capture cookie -> on
* 밑에 install누르기
* c9 aws에서 지금 JSON나오고있는 화면 url을 복사 (끝이 amazon.com으로 끝나야)

![](C:\Users\tgb03\Desktop\TIL\Django REST Framework\포스트맨설정1.PNG)

* 다음 request설정

![](C:\Users\tgb03\Desktop\TIL\Django REST Framework\포스트맨 설정2.PNG)

---

### 정리

* 기존 방식

![](C:\Users\tgb03\Desktop\TIL\Django REST Framework\기존 방식 정리1.PNG)

![](C:\Users\tgb03\Desktop\TIL\Django REST Framework\기존 방식 정리2.PNG)



### 결론

개발자는 url에 뭐가 있는지 모름. 데이터 알게하기 위해 Documentation필요. 좋은 API등이 있다.

![](C:\Users\tgb03\Desktop\TIL\Django REST Framework\결론 개발자가 데이터를 읽게 하기 위해 documentation필요.PNG)
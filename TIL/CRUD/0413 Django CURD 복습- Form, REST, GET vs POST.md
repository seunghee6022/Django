# 0413 Django CURD 복습 - Form, REST, GET vs POST

* Form
  *  HTML form을 python코드로 구현
  * 유효성 검사를 쉽게 할 수 있다. validators
  * Form/ModelForm
    * Form : 직접 필드를 정의 해야함. 위젯 설정도필요
    * ModelForm : 모델과 필드를 지정하면 django가 알아서 폼 필드를 생성

* GET/ POST

* REST

  * 2000년에 조이 필딩이 박사논문으로 소개

  * 웹의 장점을 최대한 활용할 수 있게 아키텍쳐로서 REST발표

  * 자원(URL) / 행위(Http Method) 표현으로 구성

  * http method : GET조회, POST생성/ PUT수정/DELETE 삭제

    ---

    

  * GET/member/delete/1 : URL에는 행위(e.g. delete)에 대한 표현이 들어가면 안됨.

  * DELETE/member/1 => REST FULL한 표현(o)

    * Django는 기본적으로 GET/POST만 
    * 다른 http method를 사용하려면 직접 middleware를 정의해서 추가하거나 Django Rest Framework를 사용

* 장고에서는
  * GET : 데이터를 조회할 때 READ only
  * POST : 데이터를 생성/수정/삭제 할 때



---

글을 새로 작성할 때 흐름

1. 주소나 링크로 (새 글 쓰기) 접근 (기본적으로 GET방식)

GET : 폼을 보여주면 된다

POST : 데이터를 확인하고 DB에 저장하면 된다.

```python
def create(request):

	if request.method == "POST":
        form = ArticleForm(request.POST)
        #폼에 들어간 데이터가 유효한지 유효성 검사를 해야함
        #안하면 일일이 폼에서 데이터를 꺼내와서 검사해야함
        if form.is_vaild():
            form.save()
            return redirect('article:index')
        
    else : #GET
        form = ArticleForm()
    #유효성 검사를 실패했을 때 이프문 밑에 폼의 내용이 context로 넘어가서 사용자가 어디서 틀렸는지 알 수 있다. 
    context = {
        'form' : form
    }
    
```




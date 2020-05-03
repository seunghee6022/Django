# 0428 N:M Homework

1.

* F ->Field가 틀림
* T -> 앱이름_클래스이름__지정한필드이름
* F , related_name 필수x, 은 필요시 작성

2.

​	(a) request.user 

​	(b) article.user.like_users.all

3.

(a)username

(b)followers

(c)filter

(d)remove

(e)add

4.

회원가입시에 쓰는 UserCreationForm이 auth.User를 참조하고 있기 때문이다.

forms.py에서 커스텀폼을 따로 만들어서 accounts.User를 참조하게 해줘야한다.

(form 을 커스텀하여 재정의 했는데 views에서 그대로 UserCreationForm을 사용했기 때문

model = get_user_model() 선언 필요)

5.

이름이 중복되기 때문에. 

user 글 작성자, like_users 좋아요한 작성자

user입장에서 내가 적은 모든 게시글의 목록을 가져올 때, user.article_set.all

like_users입장에서 해당 유저(내)가 좋아요 누른 모든 아티클에 대한 목록 가져올 떄, user.article_set.all해야함.

유저에서 접근도 article_set, like_users에서의 접근도 article_set이므로

그 중 하나의 이름을 related_article로 변경해줘야

6.

a)person.follwings.all

b)person.followers.all

c) request.user/ user

d) person

e)person.username
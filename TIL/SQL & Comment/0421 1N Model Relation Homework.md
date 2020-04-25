# 0421 1:N Model Relation Homework

1. i가 있으면 구별한다

__icontains : 대소문자 구별o 포함하는 단어 가진 것 반환

__contains : 대소문자 구별x 포함하는 단어 가진 것 반환

__exact : 똑같은거 찾기, 사실상 =와 같다

__iexact : 대소문자 구별 x

__in : 배열이나 문자열에 해당하는 것이 있으면 반환

__gte : grater than equal ~이상의 값



2.

* models.CASCADE - 해당 객체(`reporter`)가 삭제 되었을 때 참조하는 객체(`articles`)도 모두 삭제

* models.PROTECT- 참조하는 객체가 존재하면 삭제 금지

* models.SET_NULL - NULL 값으로 치환. NOT NULL 옵션이 있는 경우는 활용할 수 없음

* models.SET_DEFAULT - 디폴트 값(`article`)을 참조하게 끔 한다.

3.

commit = false

article

4.

템플릿에서 불러올 때는 ()붙이지 않는다.

post.comment_set.all








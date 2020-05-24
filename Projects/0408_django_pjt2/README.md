# 0408 Django_project2

* 어려웠던점
  1. delete함수를 view에서 구현할 때,  POST방식으로 해야한다는 것을 잊고 GET방식으로 할려고 해서 그것을 깨닫고 고치기까지 어려움을 겪었습니다.
  2. if  request.resolver_match.url_name을 사용하여 update랑 create일 때를 나눠서 생각하는 것을 구현하는데 어려움을 겪었습니다.
  3. 높은 rank부터 정렬하고 싶어서 object.ordered_by를 사용하여 -rank순으로 정렬하는 데도 조금 수정이 필요했습니다.
* 구현 방법

1. 기존 u->v->t 방법대로 코드를 짜준뒤, 명세서에 따라 model을 정의합니다.
2. forms.py를 만들어서 나중에 bootstrap4를 공식 문서 방법에 따라 설치하고, 로드, {%bootstrap_form form%}을 넣으면 폼이 이쁘게 변형됩니다.
3. 그 외 디자인등은 bootstrap으로 꾸밉니다.

(다음에 더 자세히 쓰겠습니다.)


# 0504 Django 마지막

### GRAVATAR

프로필 이미지 웹사이트 : `GRAVATAR`



* md5 -> hashlib : 원하는 이미지 받기 위해 해시코드 url만들어야

![image-20200504103007433](C:\Users\tgb03\AppData\Roaming\Typora\typora-user-images\image-20200504103007433.png)

* 파이썬 활용한 코드

```python
import hashlib
hashlib.md5(email.encode('UTF-8')).hexdigest()
```



### NAVBAR에 프로필이미지 가지고 오기

![image-20200504103241925](C:\Users\tgb03\AppData\Roaming\Typora\typora-user-images\image-20200504103241925.png)

base.html Navbar에서 해시값을 변경하는 코드를 만들어줘야 유저마다 다른 프로필 사진을 띄울 수 있다. ->view에서 만들어서 넘겨줘야



* views.py

> email_hash만들어서 base.html에 넘기기

![image-20200504103430409](C:\Users\tgb03\AppData\Roaming\Typora\typora-user-images\image-20200504103430409.png)

* gravata template만들기 -> {% load gravatar %}해줘야

> 하는 이유 : 다른 페이지에 들어가도 상단 네브바에서 프로필이 깨지는 것을 방지하기 위함.
>
> @stringfilter : string인거 강조 위해서. 없어도 무방

![image-20200504104319911](C:\Users\tgb03\AppData\Roaming\Typora\typora-user-images\image-20200504104319911.png)

![image-20200504104410644](C:\Users\tgb03\AppData\Roaming\Typora\typora-user-images\image-20200504104410644.png)

* 이메일을 받아서 다 url로 변경시키는 걸로 바꾸기

![](C:\Users\tgb03\AppData\Roaming\Typora\typora-user-images\image-20200504104536985.png)

그럼 이제

![image-20200504104612608](C:\Users\tgb03\AppData\Roaming\Typora\typora-user-images\image-20200504104612608.png)

이렇게 사용 가능(서버껐다가 켜서 리로드.)

gravatar 함수 파일을 로드하고 실행한다. {% load gravatar%}필수

그리고 뷰에 코드들 지워야함.

![image-20200504104710322](C:\Users\tgb03\AppData\Roaming\Typora\typora-user-images\image-20200504104710322.png)

![image-20200504105401502](C:\Users\tgb03\AppData\Roaming\Typora\typora-user-images\image-20200504105401502.png)

> @property 사용 -> profile_url대신 gravatar_url 사용 가능



#### 언제 property 사용? 언제 templte사용?

> @property 사용 -> profile_url대신 gravatar_url 사용 가능

> 특정 모델에 연관된 값을 통해 views.py랑 템플릿 동시에 활용할 때 -> property직접 지정활용. __한마디로 view.py에서 사용하고 싶을때__

>  그게 아니라 그냥 템플릿에서만 활용할 때 -> filter 사용

![image-20200504105720116](C:\Users\tgb03\AppData\Roaming\Typora\typora-user-images\image-20200504105720116.png)

![image-20200504105800202](C:\Users\tgb03\AppData\Roaming\Typora\typora-user-images\image-20200504105800202.png)

![image-20200504105401502](C:\Users\tgb03\AppData\Roaming\Typora\typora-user-images\image-20200504105401502.png)

![image-20200504105903473](C:\Users\tgb03\AppData\Roaming\Typora\typora-user-images\image-20200504105903473.png)


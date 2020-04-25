1. django에서 기본적으로 사용하는 User 모델은 AbstractUser 모델을 상속받아 정의된다.

- 아래의 models.py를 참고하여 User 모델에서 사용할 수 있는 칼럼 중 BooleanField로 정의 된 칼럼을 모두 작성하시오.

  -> is_active(), is_staff()

2. django에서 기본적으로 사용하는 User 모델의 사용할 수 있는 칼럼 중 username에 저장할 수 있는 최대 길이를 작성하시오. 

   -> 150

3. 다음은 로그인 기능을 구현한 코드이다. 빈 칸에 들어갈 코드를 작성하시오.

   (a) AuthenticationForm

   (b) login

   (c) form.get_user()

   

4. 로그인 했는지 확인하기 위하여 User 모델 내부에 정의된 속성의 이름을 작성하시오.

   -> is_authenticated

5. 로그인을 하지 않았을 경우 template에서 user 변수를 출력했을 때 나오는 클래스의 이름을 작성하시오.

6.  django에서 기본적으로 사용하는 User 모델에서 암호화를 하기 위해 사용되는 알고리즘의 이름을 작성하시오.

7.  로그아웃 기능을 구현하기 위하여 다음과 같이 코드를 작성하였다. 로그아웃 기능을 실행 시 문제가 발생한다고 할 때 그 이유와 해결 방법을 작성하시오.

   -> view의 logout함수와 이름이 같아 재귀가 발생한다.

   ->해결 방법: logout모듈을 import할 때 이름을 다르게 설정해준다.

   e.g.

   ```python
    from djano.contrub.auth import logout as auth_logout
   
   		def logout(request):
   
   				auth_logout(request)
   
   				return redirect('accounts:login')
   ```

   

   
# 0504 Django 전반적인 내용 정리 homework

1.  Django는 MTV로 이루어진 Web Framework다. MTV가 무엇의 약자이며 Django에서 각각 어떤 역할을 하고 있는지 작성하시오.

* Model(Model) - DB , 데이터 저장
* Template(View) - html 보여지는 부분 담당, 데이터를 유저한테 보여주는 역할
* View(Control) - control 담당

2. (a) articles (b)views (c)views.index

3. (a)settings.py (b)TEMPLATES (c)STATICFILES_DIRS

4. 

   >마이그레이션 생성 : `python manage.py makemigrations`
   >- 마이그레이션 DB 반영 여부 확인 : `python manage.py showmigrations`
   >- 마이그레이션에 대응되는 SQL문 출력 : `python manage.py sqlmigrate`
   >
   >- 마이그레이션 파일의 내용을 DB에 최종 반영 : `python manage.py migrate`

   * # 마이그레이션 파일 생성
     $ python manage.py makemigrations <app-name>

     # 마이그레이션 적용
     $ python manage.py migrate <app-name>

     # 마이그레이션 적용 현황
     $ python manage.py showmigrations <app-name>

     # 지정 마이그레이션의 SQL 내역
      python manage.py sqlmigrate <app-name> <migration-name>

5. * F
   * T
   * F
   * T

6. * static관련 설정 2가지
   * MEDIA_URL 파일의 주소만들기
   * MEDIA_ROOT 

   ```python
   STATIC_URL = '/static/'
   STATICFILES_DIR = [os.path.join(BASE_DIR, 'static')]
   ```

   

7. * T
   * F
   * T
   * T, -> .table : sqplite에서만 동작하고 사용하는 명령어. DML/DDL/DCL이 SQL
   * F
8. PROTECT - ProtectedError
9. (a)ManyToManyField (b)related_name, Board에서 user를 user와 like_users에서 참조하는데, 역참조시에 둘다 board_set을 사용해서 충돌하기에 related_name을 지정해야함.
10. accounts_user, accounts_user_followers
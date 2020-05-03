# 0420 Database & SQL

### RDB(Relational DataBase)

---



#### 기본 용어

* 스키마 - 관계형 데이터베이스에서 구조와 제약조건에 관련한 전반적인 명세를 기술 한 것 
* 테이블 -  열과 행의 모델을 사용해 조직된 데이터 요소들의 집합 
* 칼럼 - 고유한 데이터 형식이 지정되는 열 
* 레코드 - 단일 구조 데이터 항목을 가리키는 행 
* 기본키 - 각 행의 고유값

---



* 열 (속성, 필드)

  * 차수 : 열의 개수

* 행 (레코드, 튜플)

  * 카디널리티 : 행의 개수 = 튜플의 개수

* 릴레이션 = 스키마 + 인스턴스

  * 릴레이션의 특징

    1. 튜플의 유일성 (내용 다 같아보여도 id라도 다름)
    2. 튜플(행)의 순서 의미 없다
    3. 속성(열)의 순서도 의미 없다

    4. 속성도 유일해야 한다.(테이블 속성에 가격, 가격 - x)
    5. 속성의 원자성(도서명안에 값 두개 안됨. 한 열에는 한개의 값만)

    (cf. 원자성 -응 한칸에 값 한개만
    유일성 그냥 완전 똑같은 속성이 있나(열), 행이 있나(튜플))

* Entity Relationship Diagram 

  * ERD설계 
  * DB설계

* Entity(개체) --> 테이블의 주제(e.g. 쇼핑몰)

  * db에 저장할 어떤 것(물리/개념/동작 다 가능)
  * 물리적 형태가 있는 것(e.g. 물건 정보, 쇼핑 회원정보)
  * 개념적인것(e.g. 쇼핑 카테고리, 보험상품)
  * 행위 적인 것(e.g. 쇼핑 주문, 물건 청구, 배송 정보)

* Property(속성) ---> 열 속성

  * entity가 가질 수 있는 정보들
  * (e.g. 물건 정보, 쇼핑 회원정보)
  * (e.g. 쇼핑 카테고리, 보험상품)
  * (e.g. 쇼핑 주문, 물건 청구, 배송 정보)

* Relationship

  * 1:1 (e.g. 교육생 정보-정승희 <-> 신상정보- 정승희)
  * 1:N (e.g. 저자 <-> 책1,책2,책3, 글 작성자 <-> 게시글1,2,3)
  * N:M (e.g. 게시글 작성자 <-> 좋아요한 사람들(그 반대로도 될 수 있으므로)--> 테이블과 테이블 간의 관계)

---



### SQL

* 종류

  * `DDL`(Data Definition Language) - 새 테이블을 정의하거나 데이터를 새로 생성 할 때 주로 사용
  * `DML`(Data Manipulation Language) - 기존의 데이터를 수정, 삭제, 조회 할 때 사용
  * `DCL`(Data Control Language) - 권한, 데이터 전체를 관리(e.g. rollback)

* `DDL(Data Definicion Language)`

  * 새 테이블을 정의하거나 데이터를 새로 생성 할 때 주로 사용

  * 명령어 : `CREATE`(테이블 정의)

    ```sql
    CREATE TABLE 테이블이름(
    
    속성이름 데이터타입[NOT NULL< DEFUALT], 속성이름 데이터타입,  
    
    속성이름 데이터타입,
    
    ...
    #아래는 optinal
    PRIMARY KEY(속성이름[,속성이름]),
    
    UNIQUE(속성이름[,속성이름]),
    
    FOREIGN KEY(속성리스트) PREFERENCE 테이블이름(속성리스트),
    
    ON DELETE/ON UPDATE,
    CONSTRAINT 이름 CHECK 조건
    
     );
    ```

    * 데이터 속성 타입

      * INTEGER

      * DECIMAL(p,s) - p: 소수점을 제외한 전체 숫자 길이, s: 소수점 이하 숫자 길이

      * FLOAT(n)  - 길이가 n인 부동 소수점

      * REAL - 부동 소수(8bytes,길이 정해져있다.)

      * CHAR(n) - 길이가 n인 문자열 

        ex) CHAR(10) - 문자 하나들어와도 10bytes로 고정

      * VARCHAR(n) - 길이가 n인 문자열

        ex) VARCHAR(10) - 문자 하나들어오면 1bytes식으로 유도리 있다.

        > CHAR vs VARCHAR
        >
        > ex) CHAR(10) - 문자 하나들어와도 10bytes로 고정 --> 유도리 x
        >
        > ex) VARCHAR(10) - 문자 하나들어오면 1bytes식 --> 유도리 O

      * BLOB(Binary Large Object) - 들어오는 바이너리값 그대로 저장

  * `ALTER` : 테이블을 변경(속성 추가/삭제, 제약조건 추가/삭제)

    ```sql
    ALTER TABLE 테이블이름;
    ADD/DROP 속성이름 데이터타입[NOT NULL or DEFUALT]
    
    ex)속성 추가 메소드 ADD
    ALTER TABLE Movie ADD created_at DATETIME;
    
    ex)속성 삭제 메소드 DROP
    ALTER TABLE Movie DROP created_at;
    ```

    

  * `DROP`  : 테이블 삭제

    ```
    DROP TABLE 테이블이름;
    ```

    

* DML

  * `INSERT`

  ```sql
  INSERT INTO 테이블이름(속성리스트)
  VALUES (속성값리스트)[,(속성값리스트),(속성값리스트)...];
  
  ex)
  INSERT INTO Movie()
  VALUES ();
  ```

  * `SELECT`

  ```sql
  SELECT 속성리스트 FROM 테이블리스트;
  
  ex)모든 속성 다 보고싶을 때
  SELECT * FROM flights;
  
  ex)특정
  SELECT flight_num,price FROM flights;
  ```

  * `UPDATE`

  특정 값을 수정

  ```sql
   UADATE 테이를이름
   SET 속성이름1=값1, 속성이름2=값2...
   [WHERE 조건];
  ```

  * `DELETE`

  저장된 데이터 삭제

  ```sql
  DELETE
  FROM 테이블이름
  [WHERE 조건];
  ```

  

* DCL

  * ROLLBACK

    * `BEGIN;`

    ```sql
    SQL문, 
    SQL문, ...
    ```

    

    * `COMMIT;` -> ROLLBACK, 진짜로 db에 반영됨.

---

#### PATTERN

* LIKE - `% vs __`

  * %아래 모두, _ _아래 글자 두개인 사람만

    cf. 김사랑, 김에스더 로 결과 확인

    ​	김% --> 김사랑, 김에스더

    ​	김_ _ --> 김사랑

* ORDER BY

* ...

---

#### 정리

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

---

### ORM vs SQL 1:1 대응 (git README 참고)

* get vs filter
  * get -  무조건 1개의 값만
  * filter - 특정 column으로 조회 -> Queryset
  
  

### LIKE

> `__lte`,`__gte`,`__lt`,`__gt`,`__startswith`,`__endswith`,`__contain`,`__icontains` ...

* 나이가 30살 이상인 사람의 인원 수

orm에서의

>대소관계
>
>`__lte`(less than equal) : `<=` 
>
>`__gte `: `>=` 
>
>`__gt` :  `>`
>
>`__lt` : `<`

```python
#ORM
User.objects.filter(age__gte=30)
print(User.objects.filter(age__gte=30).query)
User.objects.filter(age__gte=30).count()
```

```sql
#sql
SELECT COUNT (*) FROM users_user
WHERE age >= 30;

COUNT(*)
43
```

* 나이가 30이면서 성이 김씨인 사람의 인원 수

> 1. 메서드 체이닝 이용(. 써서 계속 메서드 이어가기)
>
> 2. 그냥 이어서 콤마로 나열하기

```
#orm -1
User.objects.filter(age=30).filter(last_name='김').count()
#orm -2
User.objects.filter(age=30, last_name='김').count()
print(User.objects.filter(age=30, last_name='김').query)

```

```
#sql
SELECT COUNT (*) FROM users_user
WHERE age =30 AND last_name = '김';
```



* 지역번호가 02로 시작하는 사람의 인원 수

>`_startswith ` : `-%`
>
>반대는 `__endswith`

```python
#orm
User.objects.filter(phone__startswith='02-').count()
#query
print(User.objects.filter(phone__startswith='02-').query)
```

```sql
#sql
SELECT COUNT (*) FROM users_user
WHERE phone LIKE '02-%';
```

* phone에 ‘123’을 포함하고 age가 30미만인 정보를 조회하시오.

> 포함 `__icontain` ,`__contain`사용
>
> * `__icontain` : 대소문자 구분
> * `__contain` : 대소문자 구분 x, 같은거 가져오기

```python
#orm
User.objects.filter(phone__icontains='123',age__lt=30).values()
```



---

#### 정렬 및 LIMIT, OFFSET

* 나이가 많은 사람 10명

```python
#orm
```

```sql
#sql
SELECT * FROM users_user
ORDER BY age DESC
LIMIT 10;
```

* 나이가 많은 사람 10명

> Queryset에서 10까지 끊기 : `[:10] `사용

```python
#orm
User.objects.order_by('-age')[:10]
#query
print(User.objects.order_by('-age')[:10].query)
```

> 내림차순 :  `DESC`

```sql
#sql
SELECT * FROM users_user
ORDER BY age DESC
LIMIT 10;
```

* 잔액이 적은 사람 10명

```python
#orm
User.objects.order_by('balance')[:10]
```

```sql
#sql
SELECT * FROM users_user
ORDER BY balance ASC
LIMIT 10;
```

* 성, 이름 내림차순 순으로 5번째 있는 사람

> 특정 번째 : `[4]`

```python
#orm
User.object.order_by('-last_name','-first_name')[4]
```

> 특정 번째 : `OFFSET`

```sql
#sql
SELECT * FROM users_user
ORDER BY last_name DESC first_name DESC
LIMIT 1 OFFSET 4;
```

---

#### 표현식

> 표현식을 위해서는 `aggregate`를 알아야 한다.
>
> `Avg`,`Sum`,...
>
> 개별 object CRUD를 django쿼리를 통해 가능.
>
> 만약 collectoin of objects == Queryset의 요약된 정보를 얻고 싶으면, aggregate 메서드를 써야 한다.

* 전체 평균 나이

```python
#orm
from django.db.models import Avg
User.objects.aggregate(Avg('age'))
```

```sql
#sql
SELECT AVG(age) FROM users_user;
```



* 김씨의 평균 나이

```python
#orm
from django.db.models import Avg
User.objects.filter(last_name='김').aggregate(Avg('age'))
```

```sql
#sql
SELECT AVG(age) FROM users_user
WHERE last_name = '김';
```



* 계좌 잔액 중 가장 높은 금액

```python
#orm
from django.db.models import Max
User.objects.aggregate(Max('balance'))
```

```sql
#sql
SELECT MAX(balance) FROM users_user;
```



* 계좌 잔액 총액

```python
#orm
from django.db.models import Sum
User.objects.aggregate(Sum('balance'))
```

```sql
#sql
SELECT SUM(balance) FROM users_user;
```



---

#### Group by

> annotate는 개별 item에 추가 필드를 구성한다.
>
> 추후 1:N 관계에서 활용된다.
>
> 개별 오브젝트에 특정한 값(괄호안)을 붙여줌- e.g. 카운트한 값
>
> annotate 영어 사전 : 주석을 달다
>
> 특정값 붙이고 싶을 때 e.g. 게시물들에 대해 댓글 수 같이 표시
>
> 1 : N 

* 지역별 인원 수

```python
#orm
#확인용
User.objects.values('country')
#정답
User.objects.values('country').annotate(Count('country'))
```

```sql
#sql
SELECT country, COUNT(country) FROM users_user
GROUP BY country;

country | COUNT(country)
```



### Update 값 수정, 변경

* 이름이 ‘김옥자’인 사람의 행정구역을 경기도로 수정하시오.

> 값을 넣어서 변경하고 save -> 동명이인일때 문제 생김

```python
#orm
p1 = User.objects.get(first_name='옥자',last_name='김')
p1.country = '경기도'
p1.save()
```

### 해결방법

> **filter로 불러와서 update하기 **

```python
User.objects.filter(first_name='옥자',last_name='김').update(country='경기도')
```

> for문 사용

```python
users =User.objects.filter(first_name='옥자',last_name='김')

for user in users:
    user.country = '경기도'
    user.save()
```

```sql
#sql
UPDATE users_user SET country ='경기도'
WHERE first_name='옥자' AND last_name='김';
```



### DELETE 삭제

* 이름이 ‘백진호’인 사람을 삭제하시오.

```python
#orm
User.objects.filter(first_name='진호',last_name='백').delete()
```

```sql
#sql
DELETE FROM users_user
WHERE last_name='백' AND first_name='진호'; ???????????????
```



### DISTICT 중복 없이

* phone이 ‘010’으로 시작하는 사람들의 행정 구역을 __중복 없이__ 조회하시오.

> 중복 없이 : `distinct()`

```python
#orm
User.objects.filter(phone__startswith='010').values('country').distinct()

```



### 가장 높, 낮은 속성값을 가진 사람 찾기



#### 주의! Max, Min을 사용하는게 아니다. order_by 사용해서 [0]번째 사람 출력!

* 제주특별자치도에 사는 사람 중 balance가 가장 많은 사람의 first_name

```python
#orm
User.objects.filter(country='제주특별자치도').order_by('-balance')[0].first_name
```


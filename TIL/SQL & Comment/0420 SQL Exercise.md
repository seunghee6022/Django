# 0420 SQL Exercise

#### DDL

터미널에서 시작하기

```python
sqlite3 db.sqlite3 
```



- `CREATE`, `DROP` ,`ALTER`

1. 테이블 생성 `CREATE`

​	`.tables`를 통해 테이블의 유무를 확인할 수 있다.

![](C:\Users\tgb03\Desktop\online-lecture\0420\exercise\1_CREATE TABLE.PNG)





*  스키마 확인

`.schema 테이블이름;` 을 통해 flights 테이블 내의 스키마(테이블 데이터 타입, 명세...)를 확인

![](C:\Users\tgb03\Desktop\online-lecture\0420\exercise\.schema table check.PNG)

* column 이쁘게 보이게

  `.mode column` 사용

![](C:\Users\tgb03\Desktop\online-lecture\0420\exercise\.mode column.PNG)

#### DML

-`INSERT`,`UPDATE`,`DELETE`,`SELECT`

2. `INSERT`로 값 넣고

* `SELECT`조회

  3. 전체 데이터 조회하기

  `SELECT * FROM 테이블이름;` : 테이블에서 모든 값 가져오기

![](C:\Users\tgb03\Desktop\online-lecture\0420\exercise\2_INSERT and SELECT.PNG)

* 특정 테이블 조회

4. 모든 waypoint 조회하기

   `SELECT waypoint from flights;`

   ![](C:\Users\tgb03\Desktop\online-lecture\0420\exercise\4_SELECT sth.PNG)

5.  항공권 가격이 600 미만인 항공편들의 id와 flight_num을 조회하시오.

   ![](C:\Users\tgb03\Desktop\online-lecture\0420\exercise\5.PNG)

6. 도착지가 Incheon이고 가격이 500 이상인 항공편의 departure를 조회하시오.

   ![](C:\Users\tgb03\Desktop\online-lecture\0420\exercise\6.PNG)

7. 항공편의 숫자부분이 0으로 시작하고 2로 끝나면서 경유지가 Beijing인 항공편들의 id와 flight_num을 조회하시오.

   ![](C:\Users\tgb03\Desktop\online-lecture\0420\exercise\7.PNG)

8.  항공편 SQ0972의 경유지를 Tokyo로 수정하시오.

   ​	`UPDATE`사용

   ![](C:\Users\tgb03\Desktop\online-lecture\0420\exercise\8.PNG)

9. 항공편 RT9122를 테이블에서 삭제하시오.

   `DELETE`사용

   ![](C:\Users\tgb03\Desktop\online-lecture\0420\exercise\9_delete.PNG)

* DDL - `DROP`

10. flights 테이블을 삭제하시오.

    `DROP`사용

    ![](C:\Users\tgb03\Desktop\online-lecture\0420\exercise\10_DROP.PNG)

    

    




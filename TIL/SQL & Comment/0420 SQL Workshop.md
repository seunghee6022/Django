# 0420 SQL Workshop

1. countries 테이블을 생성

   ![](C:\Users\tgb03\Desktop\online-lecture\0420\workshop\1_create table.PNG)

2. 데이터 입력

   ![](C:\Users\tgb03\Desktop\online-lecture\0420\workshop\2_insert data.PNG)

3. 테이블 이름을 hotels로 변경

   `ALTER TABLE 기존이름 RENAME TO 바꿀이름`

   ![](C:\Users\tgb03\Desktop\online-lecture\0420\workshop\3_change table name.PNG)

4.  객실 가격을 내림차순으로 정렬하여 상위 2개의 room_num와 price를 조회하시오.

   ![](C:\Users\tgb03\Desktop\online-lecture\0420\workshop\4_order by desc, limit.PNG)

5.  grade 별로 분류하고 분류된 grade 개수를 내림차순으로 조회하시오.

   `group by` , `order by count(grade)` 사용!

   ![](C:\Users\tgb03\Desktop\online-lecture\0420\workshop\5_group by, count(grade).PNG)

6. 객실의 위치가 지하 혹은 등급이 deluxe인 객실의 모든 정보를 조회하시오.

   ![](C:\Users\tgb03\Desktop\online-lecture\0420\workshop\6_like.PNG)

7. 지상층 객실이면서 2020년 1월 4일에 체크인 한 객실의 목록을 price 오름차순으로 조회하시오.

   `not like` 사용!

![](C:\Users\tgb03\Desktop\online-lecture\0420\workshop\7_not like.PNG)
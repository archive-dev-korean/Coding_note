***헷갈리거나 암기 사항***
----

- substr -> 문자열에서 특정 위치의 일부를 추출할 떄 사용(oracle)
  - substring -> MYSql에서 사용(같은 기능)
- 집계함수 -> where 절에서 사용 불가능, select, having절에서는 사용 가능
- case -> select 절에서 사용 가능
- datediff 사용법 -> datediff(컬럼명1, 컬럼명2) = 컬럼명1 - 컬럼명2 (mysql 전용) -> 일 추출됨
    - 시간까지 추출하고 싶으면 TIMESTAMPDIFF 쓰면 시간까지 추출됨
      - TIMESTAMPDIFF(DAY, 컬럼1, 컬럼2) 이렇게 써도 일 추출할 수 있음
  - oracle에서 같은 기능 사용하고 싶으면 date1 - date2 하면 됨 (하지만 mysql에서도 사용 가능함)
- 문자열을 날짜 형식으로 바꿀 때
  - To_date : orcle 전용 TO_DATE('1234-08-22' ,'YYYY-mm-dd')이렇게 씀
  - STR_TO_DATE : mysql 전용  STR_TO_DATE(문자열, 포맷) 형식으로 씀
# NULL 처리 함수
---

- nullif 같으면 null로 변환 nullif(expr1, expr2) expr1 과 expr2 가 같으면 null
- IFNULL **`MYSQL 전용`** expr1이 null이면 expr2 반환 아니면 그대로 expr1 반환
- coalesce(expr1, expr2, expr3, ...) 왼쪽부터 순서대로 검사해서 처음으로 null이 아닌 값을 반환
- NVL **`ORCLE 전용`** IFNULL과 같은 기능
- NVL2(expr, 'null이 아니면 변환할 값','null일때 변환 할 값')

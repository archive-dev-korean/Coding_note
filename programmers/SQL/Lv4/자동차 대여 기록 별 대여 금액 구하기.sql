-- 문제 : CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서 자동차 종류가 '트럭'인 자동차의 대여 기록에 대해서 대여 기록 별로 대여 금액(컬럼명: FEE)을 구하여 대여 기록 ID와 대여 금액 리스트를 출력하는 SQL문을 작성해주세요. 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 대여 기록 ID를 기준으로 내림차순 정렬해주세요.
-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/151141

-- 오답 쿼리 : 
 SELECT distinct h.HISTORY_ID, case
 when h.END_DATE - h.START_DATE >=90 then round(c.DAILY_FEE * 0.9 * (h.END_DATE - h.START_DATE),0)
 when h.END_DATE - h.START_DATE >=30 then round(c.DAILY_FEE * 0.93 * (h.END_DATE - h.START_DATE),0)
 when h.END_DATE - h.START_DATE >=7 then round(c.DAILY_FEE * 0.95 * (h.END_DATE - h.START_DATE),0)
 else null
 end as FEE
 from CAR_RENTAL_COMPANY_CAR c 
 join CAR_RENTAL_COMPANY_RENTAL_HISTORY h 
 on c.CAR_ID = h.CAR_ID
 join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p 
 on c.CAR_TYPE = p.CAR_TYPE
 where p.CAR_TYPE ='트럭'

-- 일단 할인율이 하드 코딩이고 datediff쓰는게 조금더 좋다. 그리고 대여일 기준으로 +1 해야 한다.
-- order by는 나중에 추가해도 된다.
-- 가장 핵심은 discount rate에 널 조건을 추가 하지 않아서 안뜨는 것도 많다..

-- 정답(cte 사용) :  
WITH tb1 as (
    SELECT h.HISTORY_ID,
    c.CAR_TYPE,
    c.DAILY_FEE,
    DATEDIFF(h.END_DATE, START_DATE) + 1 as 'DAY',
    CASE
        WHEN DATEDIFF(h.END_DATE, START_DATE) + 1 >= 90 THEN '90일 이상'
        WHEN DATEDIFF(h.END_DATE, START_DATE) + 1 >= 30 THEN '30일 이상'
        WHEN DATEDIFF(h.END_DATE, START_DATE) + 1 >= 7 THEN '7일 이상'
        ELSE '7일 미만'
    END AS 'RENT_DAY'
    FROM CAR_RENTAL_COMPANY_CAR c
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h ON h.CAR_ID = c.CAR_ID
    WHERE CAR_TYPE = '트럭'

)

SELECT
t.HISTORY_ID,
FLOOR((DAILY_FEE * (100 - IFNULL(p.DISCOUNT_RATE,0))/100) * t.DAY) as 'FEE'
FROM tb1 t
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p ON t.CAR_TYPE = p.CAR_TYPE
AND t.RENT_DAY = p.DURATION_TYPE
ORDER BY FEE DESC, t.HISTORY_ID DESC

-- 이게 가장 깔끔하게 작성한 것 같은데
-- 내가 작성한 코드는 아니고 다른 사람이 작성한 코드 이다. 일단 보면 이해는 가는데 내가 왜 이걸 생각 못했지? 약간 이런 느낌이다.
-- cte 사용에 조금 더 익숙해 져야 할듯 하다. 그리고 오랜만에 sql 풀었는데 조금더 자주 풀어야 할 것 같기도 하다.

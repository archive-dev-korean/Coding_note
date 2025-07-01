--문제 : FOOD_PRODUCT와 FOOD_ORDER 테이블에서 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회하는 SQL문을 작성해주세요. 이때 결과는 총매출을 기준으로 내림차순 정렬해주시고 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬해주세요
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131117

--오답 :
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, (o.amount * p.price) as TOTAL_SALES
from FOOD_PRODUCT p join FOOD_ORDER o
on p.PRODUCT_ID = o.PRODUCT_ID
where o.PRODUCE_DATE like '2022-05%'

order by 3 desc, 1 asc

--얼핏 보면 조건에 부합하는 쿼리 같지만 총매출의 계산값이 이상하고 group by 옵션이 빠졌다.

--정답 :
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, sum(o.amount * p.price) as TOTAL_SALES
from FOOD_PRODUCT p join FOOD_ORDER o
on p.PRODUCT_ID = o.PRODUCT_ID
where o.PRODUCE_DATE like '2022-05%'
group by 1
order by 3 desc, 1 asc

--문제 FOOD_WAREHOUSE 테이블에서 경기도에 위치한 창고의 ID, 이름, 주소, 냉동시설 여부를 조회하는 SQL문을 작성해주세요. 이때 냉동시설 여부가 NULL인 경우, 'N'으로 출력시켜 주시고 결과는 창고 ID를 기준으로 오름차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131114

SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, ifnull(FREEZER_YN, 'N') as FREEZER_YN
from FOOD_WAREHOUSE
where ADDRESS like '%경기도%'
order by WAREHOUSE_ID asc

--오답
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS,  FREEZER_YN
from FOOD_WAREHOUSE
where ADDRESS like '%경기도%' and ifnull(FREEZER_YN, 'N') 
order by WAREHOUSE_ID asc
--> 이러면 FREEZER_YN값이 'Y'인 값만 출력됨.

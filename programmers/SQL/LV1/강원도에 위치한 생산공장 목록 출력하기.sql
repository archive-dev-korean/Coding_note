--문제 : FOOD_FACTORY 테이블에서 강원도에 위치한 식품공장의 공장 ID, 공장 이름, 주소를 조회하는 SQL문을 작성해주세요. 이때 결과는 공장 ID를 기준으로 오름차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131112

SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
from FOOD_FACTORY 
where ADDRESS like '%강원도%'
order by FACTORY_ID asc

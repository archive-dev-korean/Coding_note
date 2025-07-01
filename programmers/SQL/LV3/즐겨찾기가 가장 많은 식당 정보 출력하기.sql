--문제 : REST_INFO 테이블에서 음식종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회하는 SQL문을 작성해주세요. 이때 결과는 음식 종류를 기준으로 내림차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131123

--오답 쿼리:
select FOOD_TYPE, REST_ID, REST_NAME, max(FAVORITES) as FAVORITES
from REST_INFO
group by 1
order by 1 desc

--정말 우연히 테스트 케이스에서 정답과 같은 값이 출력되었음. 하지만 이 쿼리의 치명적인 문제는 중복 처리임.
--같은 FAVORITES 값이 있을 땐 임의의 값이 출력됨.

--정답 쿼리:
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from REST_INFO 
where (FOOD_TYPE,FAVORITES) in (
select FOOD_TYPE,max(FAVORITES)
from REST_INFO
group by FOOD_TYPE)
order by 1 desc

--서브 쿼리에 in 절을 사용해서 조건에 모두 부헙하는 값만 출력하도록 수정 이러면 중복처리 확실히 가능

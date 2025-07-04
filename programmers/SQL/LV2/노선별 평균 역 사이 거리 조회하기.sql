--문제 : SUBWAY_DISTANCE 테이블에서 노선별로 노선, 총 누계 거리, 평균 역 사이 거리를 노선별로 조회하는 SQL문을 작성해주세요.
--총 누계거리는 테이블 내 존재하는 역들의 역 사이 거리의 총 합을 뜻합니다. 총 누계 거리와 평균 역 사이 거리의 컬럼명은 각각 TOTAL_DISTANCE, AVERAGE_DISTANCE로 해주시고, 총 누계거리는 소수 둘째자리에서, 평균 역 사이 거리는 소수 셋째 자리에서 반올림 한 뒤 단위(km)를 함께 출력해주세요.
--결과는 총 누계 거리를 기준으로 내림차순 정렬해주세요.

--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/284531

--오답 쿼리: 
select ROUTE, concat(round(sum(D_BETWEEN_DIST) ,2), 'km') as TOTAL_DISTANCE, concat(round(avg(D_BETWEEN_DIST) ,3) ,'km') as AVERAGE_DISTANCE
from SUBWAY_DISTANCE 
group by ROUTE
# order by TOTAL_DISTANCE desc

--round 함수 잘못 써서 2번쨰자리 까지 반올림, 3번째 자리까지 반올림으로 적용되어서 틀림, 또한 order by에 total_distance 쓰면 문자열 기준으로 정렬되엇 틀림

--정답 쿼리:

select ROUTE, concat(round(sum(D_BETWEEN_DIST) ,1), 'km') as TOTAL_DISTANCE, concat(round(avg(D_BETWEEN_DIST) ,2) ,'km') as AVERAGE_DISTANCE
from SUBWAY_DISTANCE 
group by ROUTE
order by sum(D_BETWEEN_DIST) desc
--모두 수정한 올바른 쿼리

--문제 : 대장균 개체의 크기를 내름차순으로 정렬했을 때 상위 0% ~ 25% 를 'CRITICAL', 26% ~ 50% 를 'HIGH', 51% ~ 75% 를 'MEDIUM', 76% ~ 100% 를 'LOW' 라고 분류합니다. 대장균 개체의 ID(ID) 와 분류된 이름(COLONY_NAME)을 출력하는 SQL 문을 작성해주세요. 이때 결과는 개체의 ID 에 대해 오름차순 정렬해주세요 . 단, 총 데이터의 수는 4의 배수이며 같은 사이즈의 대장균 개체가 서로 다른 이름으로 분류되는 경우는 없습니다.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/301649

--오답 1(비율 직접 계산 해서 구함) : 
 select ID, 
 case
 when round(SIZE_OF_COLONY * 100.0 / sum(SIZE_OF_COLONY) over(),0) between 0 and 25 then 'CRITICAL'
 when round(SIZE_OF_COLONY * 100.0 / sum(SIZE_OF_COLONY) over(),0) between 26 and 50 then 'HIGH'
 when round(SIZE_OF_COLONY * 100.0 / sum(SIZE_OF_COLONY) over(),0) between 51 and 75 then 'MEDIUM'
 else 'LOW'
 end as COLONY_NAME
 from ECOLI_DATA 
 order by 1

--문제점: 일단 누적 비율이 아니라 틀리고 이렇게 계산하면 실수할 확률 올라감 시간도 오래 걸리고

--오답2(비율 누적 계산):
 SELECT
   ID,
   CASE
     WHEN PCT <= 25 THEN 'CRITICAL'
     WHEN PCT <= 50 THEN 'HIGH'
     WHEN PCT <= 75 THEN 'MEDIUM'
     ELSE 'LOW'
   END AS COLONY_NAME
 FROM (
   SELECT *,
     ROUND(
       SUM(SIZE_OF_COLONY) OVER (ORDER BY SIZE_OF_COLONY DESC) * 100.0 
       / SUM(SIZE_OF_COLONY) OVER (),
       0
     ) AS PCT
   FROM ECOLI_DATA
 ) AS SUB
 ORDER BY ID;

--누적 비율 계산 해서 구했지만 잘못 계산할 경우 결과값이 이상하게 나옴

--정답 : 
select ID,
case ntile_quartile
when 1 then "CRITICAL"
when 2 then "HIGH"
when 3 then "MEDIUM"
else "LOW"
end as COLONY_NAME
from (
select ID,
NTILE(4) over(ORDER by SIZE_OF_COLONY desc) as ntile_quartile
    from ECOLI_DATA ) sub
    order by 1

--NTILE 함수 사용해서 값을 나누면 올바르고 빠르게 계산 가능

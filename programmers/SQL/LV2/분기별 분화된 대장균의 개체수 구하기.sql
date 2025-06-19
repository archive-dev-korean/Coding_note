--문제 : 각 분기(QUARTER)별 분화된 대장균의 개체의 총 수(ECOLI_COUNT)를 출력하는 SQL 문을 작성해주세요. 이때 각 분기에는 'Q' 를 붙이고 분기에 대해 오름차순으로 정렬해주세요. 대장균 개체가 분화되지 않은 분기는 없습니다.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/299308

select 
case
when month(DIFFERENTIATION_DATE) between '01' and '03' then '1Q'
when month(DIFFERENTIATION_DATE) between '04' and '06' then '2Q'
when month(DIFFERENTIATION_DATE) between '07' and '09' then '3Q'
when month(DIFFERENTIATION_DATE) between '10' and '12' then '4Q'
end as QUARTER, count(*) as ECOLI_COUNT
from ECOLI_DATA
group by QUARTER
order by QUARTER asc

--오답 할 뻔한 개념 : group by 대신에 partition 함수 쓸 뻔 했음

--윈도우 함수 써서 푼것
SELECT DISTINCT QUARTER,
       COUNT(*) OVER (PARTITION BY QUARTER) AS ECOLI_COUNT
FROM (
  SELECT *,
    CASE
      WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 1 AND 3 THEN '1Q'
      WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 4 AND 6 THEN '2Q'
      WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 7 AND 9 THEN '3Q'
      WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 10 AND 12 THEN '4Q'
    END AS QUARTER
  FROM ECOLI_DATA
) AS sub
ORDER BY QUARTER;

--연습용으로 윈도우 함수 써보는게 좋을 것 같음

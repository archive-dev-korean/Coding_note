--문제 : 분화된 연도(YEAR), 분화된 연도별 대장균 크기의 편차(YEAR_DEV), 대장균 개체의 ID(ID) 를 출력하는 SQL 문을 작성해주세요. 분화된 연도별 대장균 크기의 편차는 분화된 연도별 가장 큰 대장균의 크기 - 각 대장균의 크기로 구하며 결과는 연도에 대해 오름차순으로 정렬하고 같은 연도에 대해서는 대장균 크기의 편차에 대해 오름차순으로 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/299310

--풀이 1: 서브 쿼리 + 조인
--풀이 2: 윈도움 함수 사용

--오답1 : 문법오류 서브쿼리 사용법 오류
select extract(year from DIFFERENTIATION_DATE) as year, year_dev, ID, 
from(select *,
   case
       when DIFFERENTIATION_DATE between '2019-01-01' and '2019-12-31' 
       then max(SIZE_OF_COLONY) - SIZE_OF_COLONY as m2019
       when DIFFERENTIATION_DATE between '2020-01-01' and '2020-12-31'
       then max(SIZE_OF_COLONY) - size_of_colony as m2020
       when DIFFERENTIATION_DATE between '2021-01-01' and '2021-12-31'
       then max(SIZE_OF_COLONY) - size_of_colony as m2021
   else null
end as year_dev
from ECOLI_DATA 
) 
------> 중간에 풀다가 뭔가 잘못됨을 깨달아서 다시 품, then 절에서는 as 를 사용할 수 없음

--오답2 : 서브쿼리로 작성 테스트 케이스 에서는 결과 정답임 하지만 제출 했을 떄 몇개의 테스트만 통과 (원인: 연도를 임의로 할당한것)
select extract(year from DIFFERENTIATION_DATE) as year, 
case
   when extract(YEAR from DIFFERENTIATION_DATE) = 2019 then m2019 - size_of_colony
   when extract(YEAR from DIFFERENTIATION_DATE) = 2020 then m2020 - size_of_colony
   when extract(YEAR from DIFFERENTIATION_DATE) = 2021 then m2021 - size_of_colony
   else null
end as year_dev, ID
from(
   select *,
   max(case when extract(YEAR from DIFFERENTIATION_DATE) = 2019 then size_of_colony end) over () as m2019,
   max(case when extract(year from DIFFERENTIATION_DATE) = 2020 then size_of_colony end) over () as m2020,
   max(case when extract(year from DIFFERENTIATION_DATE) = 2021 then size_of_colony end) over () as m2021
       from ECOLI_DATA
       ) as sub
order by year asc, year_dev asc

--정답 1 : 서브쿼리와 join활용 -> 비추천, 논리 구조 어려움
SELECT 
  YEAR(e.DIFFERENTIATION_DATE) AS YEAR,
  (m.MAX_SIZE - e.SIZE_OF_COLONY) AS YEAR_DEV,
  e.ID
FROM ECOLI_DATA AS e
JOIN (
  SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS MAX_SIZE
  FROM ECOLI_DATA
  GROUP BY YEAR
) AS m
  ON YEAR(e.DIFFERENTIATION_DATE) = m.YEAR
ORDER BY YEAR ASC, YEAR_DEV ASC;


-- 정답 2 : 윈도우 함수 사용 제일 추천, 간단 
-- 참고사항 mysql에서는 year() 함수 지원하지만 다른 rdbms에서는 extract를 쓰기 떄문에 extract를 쓰는 걸 추천!
SELECT 
  YEAR(DIFFERENTIATION_DATE) AS YEAR,
  MAX(SIZE_OF_COLONY) OVER (PARTITION BY YEAR(DIFFERENTIATION_DATE)) - SIZE_OF_COLONY AS YEAR_DEV,
  ID
FROM ECOLI_DATA
ORDER BY YEAR ASC, YEAR_DEV ASC;

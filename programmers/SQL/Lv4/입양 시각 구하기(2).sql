-- 문제 : 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59413

SELECT 
HOUR(DATETIME) as HOUR,
COUNT(*) as count
from ANIMAL_OUTS 
group by HOUR
order by 1

-- 내가 적은 답은 이건데 사실 이 것도 목적을 보면 틀린답은 아니다 하지만 문제에서 조금 더 정교하게 0일떄도 출력하도록 요구 하고 있으니

-- 다르게 풀어보면

SELECT 
  h.hour AS HOUR,
  COUNT(a.DATETIME) AS count
FROM (
  SELECT 0 AS hour UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL
  SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL
  SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10 UNION ALL SELECT 11 UNION ALL
  SELECT 12 UNION ALL SELECT 13 UNION ALL SELECT 14 UNION ALL SELECT 15 UNION ALL
  SELECT 16 UNION ALL SELECT 17 UNION ALL SELECT 18 UNION ALL SELECT 19 UNION ALL
  SELECT 20 UNION ALL SELECT 21 UNION ALL SELECT 22 UNION ALL SELECT 23
) AS h
LEFT JOIN ANIMAL_OUTS a
  ON HOUR(a.DATETIME) = h.hour
GROUP BY h.hour
ORDER BY h.hour

-- 이렇게 풀 수 있지만 매우 비추천하고

-- 재귀 cte 쓰면 된다.
WITH RECURSIVE OUTS AS (
  SELECT 0 AS N

  UNION ALL

  SELECT N+1
  FROM OUTS
  WHERE N < 23)

SELECT O.N AS HOUR, COUNT(ANIMAL_ID) AS COUNT
FROM OUTS O
LEFT JOIN ANIMAL_OUTS A ON O.N = HOUR(A.DATETIME)
GROUP BY HOUR
ORDER BY HOUR ASC

-- 음 조금 이해하기 어려울수 있는데 위에 처럼 쓰는 것보다 훨씬 효율적이다.

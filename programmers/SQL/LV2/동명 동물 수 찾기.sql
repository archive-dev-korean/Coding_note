--문제 : 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59041

--정답 1(group by, having 사용) : 
SELECT NAME, count(*) as count
from ANIMAL_INS
where NAME is not null 
group by 1
having count(*) >= 2
order by 1

--정답 2(윈도우 함수 사용) : 
SELECT DISTINCT NAME, name_count
FROM (
    SELECT NAME,
           COUNT(NAME) OVER (PARTITION BY NAME) AS name_count
    FROM ANIMAL_INS
    WHERE NAME IS NOT NULL
) AS counted
WHERE name_count > 1;

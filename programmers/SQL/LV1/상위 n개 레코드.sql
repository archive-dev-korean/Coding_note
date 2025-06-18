--문제 : 동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59405

--풀이1 : 
SELECT NAME
from ANIMAL_INS 
order by DATETIME asc
limit 1

--풀이 2 : 
select NAME
from ANIMAL_INS
where DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS)

--아까와 마찬가지로 집계함수 쓰는게 더 효율적(데이터 많을 시) 

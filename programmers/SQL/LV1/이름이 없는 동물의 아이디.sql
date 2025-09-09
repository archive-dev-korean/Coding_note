--문제 : 동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59039

SELECT ANIMAL_ID
from ANIMAL_INS 
where isnull(NAME)

-- #이렇게 쓰는게 더 효과적
select animal_id
from animal_ins
where name is null

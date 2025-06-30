--문제 : 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다."
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59408

SELECT count(distinct NAME) as count
from ANIMAL_INS 
where NAME is not null 

--처음에 distinct count(NAME) as count 했을 때는 의미 없었지만 distinct 컬럼명 쓰면 중복 처리 잘 됨

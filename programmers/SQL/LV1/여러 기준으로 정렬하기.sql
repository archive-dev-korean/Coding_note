--문제 : 동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59404

SELECT ANIMAL_ID, NAME, DATETIME
from ANIMAL_INS 
order by NAME asc, DATETIME desc

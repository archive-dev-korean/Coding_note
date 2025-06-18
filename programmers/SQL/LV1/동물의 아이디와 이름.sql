--문제 : 동물 보호소에 들어온 모든 동물의 아이디와 이름을 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요. SQL을 실행하면 다음과 같이 출력되어야 합니다.(아이디 기준 오름차순)
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59403

SELECT ANIMAL_ID, NAME
from ANIMAL_INS 
order by ANIMAL_ID 
--oder by에서 방향 생략하면 오름차순 (asc 써도 되고 안써도 됨)

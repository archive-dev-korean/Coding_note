--문제 : 동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요. SQL을 실행하면 다음과 같이 출력되어야 합니다.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59034

SELECT *
from ANIMAL_INS 
order by ANIMAL_ID

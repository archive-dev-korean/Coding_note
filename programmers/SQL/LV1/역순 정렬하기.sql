--문제 : 동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 ANIMAL_ID 역순으로 보여주세요. SQL을 실행하면 다음과 같이 출력되어야 합니다.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59035

SELECT NAME, DATETIME
from ANIMAL_INS 
order by ANIMAL_ID desc

--문제 : 동물 보호소에 들어온 동물 중 아픈 동물1의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59036

SELECT ANIMAL_ID, NAME
from ANIMAL_INS 
where INTAKE_CONDITION ='sick'

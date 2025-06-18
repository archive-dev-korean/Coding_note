--문제 : ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다. 동물 보호소에 들어온 동물 중, 이름이 있는 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59407

SELECT ANIMAL_ID
from ANIMAL_INS 
where name is not null
order by ANIMAL_ID 
--order by 방향 명시적으로 적어도 되고 안적어도 됨 안적으면 디폴트 값이 오름차순 

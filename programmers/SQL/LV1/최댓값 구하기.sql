--문제 : ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다. 가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59415

--두가지 풀이
--풀이 1 : order by 사용
select DATETIME as 시간
from ANIMAL_INS
order by DATETIME desc
limit 1;

--풀이 2: max사용
select max(Datetime) as 시간
from ANIMAL_INS

--orde by를 사용할 시 자료 전체를 조회하고 그 중 하나를 골라내기 떄문에 큰 테이블에서는 성능 저하 발생
--max를 쓰는게 바람직

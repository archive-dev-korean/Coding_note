--문제: DEVELOPER_INFOS 테이블에서 Python 스킬을 가진 개발자의 정보를 조회하려 합니다. Python 스킬을 가진 개발자의 ID, 이메일, 이름, 성을 조회하는 SQL 문을 작성해 주세요. 결과는 ID를 기준으로 오름차순 정렬해 주세요.
--출처: https://school.programmers.co.kr/learn/courses/30/lessons/276013

--python 기술을 가진 사람은 order by를 사용해 ID로 오름차순
select ID, EMAIL, FIRST_NAME, LAST_NAME 
from DEVELOPER_INFOS
where SKILL_1='Python'or
SKILL_2='Python'or
SKILL_3='Python'
order by ID ASC

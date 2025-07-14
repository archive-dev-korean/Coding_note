--문제 : DEVELOPERS 테이블에서 Front End 스킬을 가진 개발자의 정보를 조회하려 합니다. 조건에 맞는 개발자의 ID, 이메일, 이름, 성을 조회하는 SQL 문을 작성해 주세요.
-- 결과는 ID를 기준으로 오름차순 정렬해 주세요.

-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/276035

--정답(cte 쿼리) : 
with sc as(
select sum(code) as FRONT_END_SUM
from SKILLCODES
where CATEGORY = 'Front End'
  )
select ID, EMAIL, FIRST_NAME, LAST_NAME
from sc, DEVELOPERS
where sc.FRONT_END_SUM & skill_code > 0

order by 1

--정답(서브쿼리 사용) : 
SELECT
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM
    DEVELOPERS
WHERE
    SKILL_CODE & (
        SELECT SUM(CODE)
        FROM SKILLCODES
        WHERE CATEGORY = 'Front End'
    ) > 0
ORDER BY
    ID ASC

--cte 사용이 편한듯 cte 사용법에 조금 더 익숙해 져야 할듯

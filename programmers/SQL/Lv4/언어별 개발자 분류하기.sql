-- 문제 : DEVELOPERS 테이블에서 GRADE별 개발자의 정보를 조회하려 합니다. GRADE는 다음과 같이 정해집니다.

-- A : Front End 스킬과 Python 스킬을 함께 가지고 있는 개발자
-- B : C# 스킬을 가진 개발자
-- C : 그 외의 Front End 개발자
-- GRADE가 존재하는 개발자의 GRADE, ID, EMAIL을 조회하는 SQL 문을 작성해 주세요.

-- 결과는 GRADE와 ID를 기준으로 오름차순 정렬해 주세요.

--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/276036

--오답 쿼리: 
 select 
 case
 when d.SKILL_CODE & 10512 > 0 then 'A'
 # when d.SKILL_CODE & sum(256,16,2048,8192) > 0 then 'A'
 when d.SKILL_CODE & 1024 > 0 then 'B'
 when d.skill_code & 10256 > 0 then 'C'
 else null
 # else d.skill_code & sum(8192,2048,16) > 0 then 'C'
 end as GRADE, d.ID, d.EMAIL
 from DEVELOPERS d
 order by 1 , 2

--직접 skillcode 테이블에서 따와서 조회해야 하는 건데 단순하게 sum만 써서 조회해서 틀림
--테스트 케이스만 맞음

--정답 쿼리1(CTE & 서브쿼리 사용) : 
 WITH SKC AS (
   SELECT 
     CASE 
       WHEN d.SKILL_CODE & (
         SELECT SUM(code) FROM SKILLCODES WHERE CATEGORY = 'Front End') >0 AND d.SKILL_CODE &(select sum(code) from SKILLCODES WHERE NAME = 'python') > 0 THEN 'A'
       WHEN d.SKILL_CODE & (
         SELECT SUM(code) FROM SKILLCODES WHERE NAME = 'C#'
       ) > 0 THEN 'B'
       WHEN d.SKILL_CODE & (
         SELECT SUM(code) FROM SKILLCODES WHERE CATEGORY = 'Front End'
       ) > 0 THEN 'C'
       ELSE null
     END AS GRADE,
     d.ID, 
     d.EMAIL
   FROM DEVELOPERS d
 )

 SELECT *
 FROM SKC
 where grade is not null
 ORDER BY GRADE, ID

--다만 이러면 연산량이 늘어나서 데이터가 클 경우 조금 시간이 많이 걸릴것

--정답2(두개의 CTE 사용) :
WITH CODE_SUM AS (
    SELECT
        (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End') AS FRONT_END,
        (SELECT SUM(CODE) FROM SKILLCODES WHERE NAME = 'Python') AS PYTHON,
        (SELECT SUM(CODE) FROM SKILLCODES WHERE NAME = 'C#') AS CSHARP
),
CTE AS (
    SELECT
        CASE
            WHEN SKILL_CODE & c.FRONT_END > 0 AND SKILL_CODE & c.PYTHON > 0 THEN 'A'
            WHEN SKILL_CODE & c.CSHARP > 0 THEN 'B'
            WHEN SKILL_CODE & c.FRONT_END > 0 THEN 'C'
        END AS GRADE,
        ID, EMAIL
    FROM DEVELOPERS, CODE_SUM c
)
SELECT *
FROM CTE
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID

--cte 테이블에서 카디션 곱을 통해 각각의 스킬을 체크 함.

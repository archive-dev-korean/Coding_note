--문제 : DEVELOPERS 테이블에서 Python이나 C# 스킬을 가진 개발자의 정보를 조회하려 합니다. 조건에 맞는 개발자의 ID, 이메일, 이름, 성을 조회하는 SQL 문을 작성해 주세요.
--결과는 ID를 기준으로 오름차순 정렬해 주세요.

--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/276034

--오답 커리 1 : 
# select ID, EMAIL, FIRST_NAME, LAST_NAME
# from DEVELOPERS 
# where skill_code & 256 = 256 or skill_code & 1024 = 1024 
# # or skill_code & 1280 = 1280
# # group by ID
# order by ID asc

--skillcode 테이블에 비트로 변환된 코드 값이 있어서 이걸 이용해서 구했지만 테스트만 통과하고 오답처리됨
--group by절사용 불필요 
--비트 연산자 오류 처리인가 싶어서 확실한 방법으로 다시 처리함

--오답 2: 
# select ID, EMAIL, FIRST_NAME, LAST_NAME
# from DEVELOPERS
# where skill_code & 1280 > 0
# order by ID asc

-- 하지만 이것도 마찬가지로 테스트만 통과하고 오답 처리됨
--원인 :  결국 skillcode 에서 해당하는 스킬 값을 가져와야 함

--오답 3:
select d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
from DEVELOPERS d,
(select code
from SKILLCODES
where NAME in ('C#', "Python")
) s
where s.code & d.SKILL_CODE > 0
order by d.ID asc

-- 잘 짜여진 코드 처럼 보이지만 서브 쿼리에서 c#과 python 스킬을 가진 사람의 코드를 둘다 가져오기 떄문에
-- 두가지 스킬을 모두 가진 사람이라면 2번씩 출력됨 결국 오답

--정답: 
select d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
from DEVELOPERS d,
(select sum(code) as code
from SKILLCODES
where NAME in ('C#', "Python")
) s
where s.code & d.SKILL_CODE > 0
order by d.ID asc

--서브 쿼리에서 code를 합쳐 주어야 올바르게 스킬 체크가 가능


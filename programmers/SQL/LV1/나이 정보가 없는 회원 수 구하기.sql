--문제 : USER_INFO 테이블에서 나이 정보가 없는 회원이 몇 명인지 출력하는 SQL문을 작성해주세요. 이때 컬럼명은 USERS로 지정해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131528

-- isnull사용해서 NULL값인 것만 카운트
SELECT count(*) as USERS
from USER_INFO 
where isnull(age)

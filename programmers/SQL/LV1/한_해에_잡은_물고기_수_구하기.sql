--문제 : FISH_INFO 테이블에서 2021년도에 잡은 물고기 수를 출력하는 SQL 문을 작성해주세요. 이 때 컬럼명은 'FISH_COUNT' 로 지정해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/298516

--Date 타입으로 되어있는 TIME컬럼에서 year항목만 추출후 문제 조건에 맞는 쿼리 작성
select count(*) as FISH_COUNT
from (
    select EXTRACT(YEAR from TIME) as ET
    from FISH_INFO
) as FS
where ET ='2021'

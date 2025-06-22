--문제 : FISH_INFO 테이블에서 잡은 BASS와 SNAPPER의 수를 출력하는 SQL 문을 작성해주세요. 컬럼명은 'FISH_COUNT`로 해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/298518

--오답 1:  ,활용 쿼리
select count(*) as FISH_COUNT
from FISH_INFO i , FISH_NAME_INFO n
where i.FISH_TYPE = n.FISH_TYPE and i.FISH_TYPE in (0,1)

--오답 2: 조인 활용 쿼리
select count(*) as FISH_COUNT
from FISH_INFO i 
join FISH_NAME_INFO n 
     on i.FISH_TYPE = n.FISH_TYPE
where n.FISH_TYPE in (0,1)

--틀린이유: 사실 위의 두 쿼리는 결과값은 문제에서 요구한 사항에 모두 부합합
--하지만 문제를 잘 읽어보면 'bBASS'와 'SNAPPER'의 수를 출력하라고 했으므로
--아래의 쿼리가 정답임

--정답 : 
select count(*) as FISH_COUNT
from FISH_INFO i
join FISH_NAME_INFO n
    on i.FISH_TYPE = n.FISH_TYPE
where n.FISH_NAME in ('BASS','SNAPPER')
--이름으로 조회해야 정답으로 인정 처리됨

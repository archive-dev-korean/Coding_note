--문제 : 천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59042

SELECT o.ANIMAL_ID, o.NAME
from ANIMAL_OUTS o left outer join ANIMAL_INS i on o.ANIMAL_ID = i.ANIMAL_ID
where i.ANIMAL_ID is null
order by 1

--아우터 조인을 활용함. 보호소에 들어온 기록이 있어야 입양을 간데이터가 생기기 떄문에(반대의 경우는 없음) 입양 기록을 기준으로 outer join하고 입양 기록엔 있지만 보호 기록은 없는 것만 추출하면 됨

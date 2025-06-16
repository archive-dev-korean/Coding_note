--문제: 잡은 물고기 중 길이가 10cm 이하인 물고기의 수를 출력하는 SQL 문을 작성해주세요. 물고기의 수를 나타내는 컬럼 명은 FISH_COUNT로 해주세요.
--출처: https://school.programmers.co.kr/learn/courses/30/lessons/293258

--LENGTH컬럼에서 길이가 10cm이하일 경우 데이터 타입이 NULL로 되어있음 그래서 NULL값만 세서 출력
select count(*) as FISH_COUNT 
from FISH_INFO
where LENGTH is NULL

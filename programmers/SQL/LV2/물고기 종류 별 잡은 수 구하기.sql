--문제 : FISH_NAME_INFO에서 물고기의 종류 별 물고기의 이름과 잡은 수를 출력하는 SQL문을 작성해주세요.
-- 물고기의 이름 컬럼명은 FISH_NAME, 잡은 수 컬럼명은 FISH_COUNT로 해주세요.
-- 결과는 잡은 수 기준으로 내림차순 정렬해주세요.

--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/293257

select count(*) as FISH_COUNT, n.FISH_NAME
from FISH_NAME_INFO n 
join FISH_INFO i
on n.FISH_TYPE = i.FISH_TYPE
group by n.FISH_NAME
order by FISH_COUNT desc

--GROUP by 사용하면 쉽게 구할 수 있음. join 사용해서 데이터 증폭

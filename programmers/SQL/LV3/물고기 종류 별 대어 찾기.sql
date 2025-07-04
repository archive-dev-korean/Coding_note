--문제 : 물고기 종류 별로 가장 큰 물고기의 ID, 물고기 이름, 길이를 출력하는 SQL 문을 작성해주세요.물고기의 ID 컬럼명은 ID, 이름 컬럼명은 FISH_NAME, 길이 컬럼명은 LENGTH로 해주세요.결과는 물고기의 ID에 대해 오름차순 정렬해주세요.단, 물고기 종류별 가장 큰 물고기는 1마리만 있으며 10cm 이하의 물고기가 가장 큰 경우는 없습니다.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/293261

--오답 1 : 
# select i.ID, n.FISH_NAME, i.LENGTH
# from FISH_INFO i join 
# FISH_NAME_INFO n on i.fish_type = n.fish_type
# group by 2
# having max(i.length)
# order by 1

--group by 절 사용 오류로 에러가 발생 group by 사용할 때는 select 절에 집계 함수가 있어야 함.

--정답 1(서브 쿼리 활용) : 
 select i.ID, n.FISH_NAME, i.LENGTH
 from FISH_INFO i join 
 FISH_NAME_INFO n on i.fish_type = n.fish_type
 where (n.FISH_NAME, i.LENGTH) in 
 (
 select n.FISH_NAME, max(i.LENGTH)
 from FISH_INFO i
 join FISH_NAME_INFO n on i.FISH_TYPE = n.FISH_TYPE
     group by 1)
 order by 1

--문제에서 요구하는게 가장큰 물고기를 출려하는게 아니라 가장 큰 물고기 중에서 id와 물고기 종류, 길이를 출력하는 것이기 때문에 서브 쿼리 사용 필요함

--정답 2(cte 사용): 
with sub as
(select n.fish_name, max(i.length) as max_length
from FISH_INFO i join 
FISH_NAME_INFO n on i.fish_type = n.fish_type
group by 1
)
select i2.ID, n2.FISH_NAME, i2.LENGTH
from FISH_INFO i2 join 
FISH_NAME_INFO n2 on i2.fish_type = n2.fish_type
join sub on n2.FISH_NAME = sub.FISH_NAME and i2.LENGTH = sub.MAX_LENGTH
order by 1

--나는 이게 조금 더 직관적으로 해석 할수 있는 것 같음. 

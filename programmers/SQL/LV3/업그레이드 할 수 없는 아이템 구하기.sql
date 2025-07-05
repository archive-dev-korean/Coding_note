--문제 : 더 이상 업그레이드할 수 없는 아이템의 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME), 아이템의 희귀도(RARITY)를 출력하는 SQL 문을 작성해 주세요. 이때 결과는 아이템 ID를 기준으로 내림차순 정렬해 주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/273712

--정답1(left join 사용) : 
select i.ITEM_ID, i.ITEM_NAME, i.RARITY
from ITEM_INFO i left join ITEM_TREE t on
i.ITEM_ID = t.PARENT_ITEM_ID
where t.parent_ITEM_ID is null
order by 1 desc

--정답 2(서브쿼리 사용) : 
select ITEM_ID, ITEM_NAME, RARITY
from ITEM_INFO
where ITEM_ID not in 
(select PARENT_ITEM_ID 
from ITEM_TREE
where parent_item_id is not null)
order by 1 desc

--둘다 써도 무방하긴 한데 서브 쿼리가 조금더 보기 편한듯 하다 개인적으로

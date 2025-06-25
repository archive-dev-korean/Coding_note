--문제 : ROOT 아이템을 찾아 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME)을 출력하는 SQL문을 작성해 주세요. 이때, 결과는 아이템 ID를 기준으로 오름차순 정렬해 주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/273710

select i.ITEM_ID, i.ITEM_NAME
from item_info i
join item_tree t on i.ITEM_ID = t.ITEM_ID
where t.parent_item_id is null
order by 1 
--아이템 아이디 끼리 조인하고 부모 아이템 아이디가 null인 경우에 root아이템 이기 떄문에 조건 주면 조회 가능 

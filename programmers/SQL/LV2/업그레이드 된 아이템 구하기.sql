--문제 : 아이템의 희귀도가 'RARE'인 아이템들의 모든 다음 업그레이드 아이템의 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME), 아이템의 희귀도(RARITY)를 출력하는 SQL 문을 작성해 주세요. 이때 결과는 아이템 ID를 기준으로 내림차순 정렬주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/273711

--오답 쿼리 :
# select distinct i.ITEM_ID, i.ITEM_NAME, i.RARITY
# from ITEM_INFO i
# join ITEM_TREE t on i.ITEM_ID = t.ITEM_ID
# where i.RARITY in ('RARE') or
# t.PARENT_ITEM_ID is not null and t.PARENT_ITEM_ID < t.ITEM_ID
# order by i.ITEM_ID desc

--item_Id 끼리 조인 하고 부모 아이템 아이디가 자식 부모 아이디 보다 작을 떄에만 조건이 성립한다고 생각함
--PARENT_ID가 없을 경우 NULL이니까 무조건 본인의 item_ID보다 작을 것이라고 생각함 그래서 NULL값 제외해서 조회 하라고 조건문을 줬지만
-- test 케이스 에서 일부 통과함 하지만 오답

--정답 쿼리:
select c.ITEM_ID, c.ITEM_NAME, c.RARITY
from ITEM_TREE t
join ITEM_INFO p on t.PARENT_ITEM_ID = p.ITEM_ID
join ITEM_INFO c on t.ITEM_ID = c.ITEM_ID
where p.RARITY = 'RARE'
order by c.ITEM_ID DESC

--자식 id와 부모 id로도 조인 하면 확실하게 원하는 조건을 얻을 수 있음.
--이걸 생각해내기가 어려운 것 같음 

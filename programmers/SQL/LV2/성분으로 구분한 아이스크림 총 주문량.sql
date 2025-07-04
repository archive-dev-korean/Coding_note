--문제 : 상반기 동안 각 아이스크림 성분 타입과 성분 타입에 대한 아이스크림의 총주문량을 총주문량이 작은 순서대로 조회하는 SQL 문을 작성해주세요. 이때 총주문량을 나타내는 컬럼명은 TOTAL_ORDER로 지정해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/133026

SELECT i.INGREDIENT_TYPE, sum(f.TOTAL_ORDER) AS TOTAL_ORDER
from FIRST_HALF f
join ICECREAM_INFO i on f.flavor = i.flavor
group by i.INGREDIENT_TYPE
order by 2 asc

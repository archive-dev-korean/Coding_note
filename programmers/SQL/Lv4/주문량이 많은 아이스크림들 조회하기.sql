-- 문제 : 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.
-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/133027

-- 정답 쿼리 : 
SELECT f.FLAVOR
from FIRST_HALF f join JULY j on f.FLAVOR = j.FLAVOR
group by f.FLAVOR
order by sum(f.TOTAL_ORDER) + sum(j.TOTAL_ORDER) desc
limit 3

-- 정답은 이건데 처음에 조인을 할떄 

from FIRST_HALF f join JULY j on f.SHIPMENT_ID = j.SHIPMENT_ID
-- 이렇게 했었다. 조인 컬럼 오류 때문에 원하는 값이 나오지 않았고, 그래서 오답 처리 되었었다.
-- 당연히 기본키라 조인해도 문제가 없을 줄 알았다. 그러나 테이블 설명을 잘 보면 각각 상반기 주문정보, 7월 주문 정보라서 shipment_id 값이같아도 다른 맛일 수도 있었다.
-- 그래서 flavor기준으로 조인하는게 맞다.

-- 또한 윈도우 함수로도 구할 수 있는데

SELECT DISTINCT FLAVOR
FROM (
    SELECT 
        f.FLAVOR,
        SUM(f.TOTAL_ORDER) OVER (PARTITION BY f.FLAVOR) + 
        SUM(j.TOTAL_ORDER) OVER (PARTITION BY j.FLAVOR) AS TOTAL_SUM
    FROM FIRST_HALF f
    JOIN JULY j ON f.FLAVOR = j.FLAVOR
) t
ORDER BY TOTAL_SUM DESC
LIMIT 3

-- 이렇게 구할 수도 있음

-- row_number() 나 rank()도 사용해서 구할 수도 있음. 방법은 윈도우 함수 방법과 똑같음.

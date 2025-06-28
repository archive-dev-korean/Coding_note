--문제 : PRODUCT 테이블과 OFFLINE_SALE 테이블에서 상품코드 별 매출액(판매가 * 판매량) 합계를 출력하는 SQL문을 작성해주세요. 결과는 매출액을 기준으로 내림차순 정렬해주시고 매출액이 같다면 상품코드를 기준으로 오름차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131533

SELECT p.PRODUCT_CODE, sum(p.price * o.sales_amount) as SALES
from PRODUCT p 
join OFFLINE_SALE o on p.PRODUCT_ID = o.PRODUCT_ID
group by 1
order by 2 desc, 1 asc

--주의 사항: 여기서 sales 정의할 떄 sum 해줘야 함 왜냐하면 다른날 같은 상품을 조회할 경우 product_Id가 2개 이상이 존재하기 떄문에 따로 집계됨

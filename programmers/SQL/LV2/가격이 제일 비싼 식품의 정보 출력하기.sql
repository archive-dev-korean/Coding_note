--문제 : FOOD_PRODUCT 테이블에서 가격이 제일 비싼 식품의 식품 ID, 식품 이름, 식품 코드, 식품분류, 식품 가격을 조회하는 SQL문을 작성해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131115

SELECT *
from FOOD_PRODUCT 
order by price desc
limit 1

-- max를 이용한 풀이
select PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
from FOOD_PRODUCT
where price =(select max(price) from FOOD_PRODUCT)

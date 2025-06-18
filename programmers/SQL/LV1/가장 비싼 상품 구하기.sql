--문제 : PRODUCT 테이블에서 판매 중인 상품 중 가장 높은 판매가를 출력하는 SQL문을 작성해주세요. 이때 컬럼명은 MAX_PRICE로 지정해주세요.
-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131697

SELECT max(price) as MAX_PRICE
from PRODUCT 

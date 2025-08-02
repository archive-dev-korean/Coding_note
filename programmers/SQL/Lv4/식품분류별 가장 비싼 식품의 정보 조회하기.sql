-- 문제 : FOOD_PRODUCT 테이블에서 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회하는 SQL문을 작성해주세요. 이때 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력시켜 주시고 결과는 식품 가격을 기준으로 내림차순 정렬해주세요.
-- 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/131116

SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN (
    SELECT CATEGORY, MAX(PRICE)
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치','식용유')
    GROUP BY CATEGORY
)
ORDER BY PRICE DESC
-- 이렇게 풀 수도 있고 

-- cte, 윈도우 함수, 등을 이용해 푸는 방법도 있다.

WITH TBL AS (
    SELECT
        CATEGORY,
        PRODUCT_NAME,
        PRICE,
        MAX(PRICE) OVER (PARTITION BY CATEGORY) AS MAX_PRICE
    FROM
        FOOD_PRODUCT
    WHERE
        CATEGORY IN ('과자', '국', '김치', '식용유')
    )

SELECT
    CATEGORY,
    MAX_PRICE,
    PRODUCT_NAME
FROM
    TBL
WHERE
    PRICE = MAX_PRICE
ORDER BY
    PRICE DESC

-- 서브 쿼리가 여기에서는 더 쉬워 보이는데 윈도우 함수나 cte의 사용법을 알고 있어야 한다 복잡한 문제로 갈 수록 쓰일 확률이 높기에

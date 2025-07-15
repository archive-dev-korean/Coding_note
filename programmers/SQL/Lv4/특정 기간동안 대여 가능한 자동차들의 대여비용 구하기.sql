--문제 : CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/157339

--오답 쿼리(cte 와 서브쿼리 활용 미완성) : 
 with car as(
 select *
 from CAR_RENTAL_COMPANY_CAR c join CAR_RENTAL_COMPANY_RENTAL_HISTORY h on c.CAR_ID = h.CAR_ID
 where h.START_DATE like '2022-11%' and c.CAR_TYPE = '세단' or c.CAR_TYPE ='SUV')

 SELECT a.CAR_ID, a.CAR_TYPE, 
 case
 when 
 end as round(a.DAILY_FEE,0) as FEE
 from CAR_RENTAL_COMPANY_DISCOUNT_PLAN p outer join car a p.CAR_TYPE = a.CAR_TYPE
 # where a.start_date - a.end_date >= 30
--작성중 뭔가 이상하단 생각이 들어서 처음부터 다시 문제를 읽고 다시 짜기 시작함
--그러다가 서브 쿼리로만으로도 결과를 낼 수 있다는 걸 알게됨

--오답(서브 쿼리 활용) : 
SELECT distinct
    c.CAR_ID, 
    c.CAR_TYPE, 
    ROUND(c.DAILY_FEE * (1 - p.DISCOUNT_RATE / 100) * 30, 0) AS FEE
FROM 
    CAR_RENTAL_COMPANY_CAR c
JOIN 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY h ON c.CAR_ID = h.CAR_ID
JOIN 
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN p ON c.CAR_TYPE = p.CAR_TYPE
WHERE 
    c.CAR_TYPE IN ('세단', 'SUV')
    AND h.START_DATE >= '2022-11-01' AND h.START_DATE < '2022-12-01'
    AND p.DURATION_TYPE = '30일 이상'
    AND ROUND(c.DAILY_FEE * (1 - p.DISCOUNT_RATE / 100) * 30, 0) >= 500000
    AND ROUND(c.DAILY_FEE * (1 - p.DISCOUNT_RATE / 100) * 30, 0) < 2000000
ORDER BY 
    FEE DESC, c.CAR_TYPE, c.CAR_ID

-- 대여 조건에서 에러가 남 대여 조건을 다시 한번 생각해 봐야겠음 문제마다 다 다르고 어떻게 하는게 가장 올바른지
-- 시작일이 11월1일 부터 11월31일까지 있는 거면 되는거 아닌가? 그럼 대여 가능 일 것이라고 생각

--정답(대여조건 변경, 서브쿼리):
SELECT distinct
    c.CAR_ID, 
    c.CAR_TYPE, 
    ROUND(c.DAILY_FEE * (1 - p.DISCOUNT_RATE / 100) * 30, 0) AS FEE
FROM 
    CAR_RENTAL_COMPANY_CAR c
JOIN 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY h ON c.CAR_ID = h.CAR_ID
JOIN 
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN p ON c.CAR_TYPE = p.CAR_TYPE
WHERE 
    c.CAR_TYPE IN ('세단', 'SUV')
    # AND h.START_DATE >= '2022-11-01' AND h.START_DATE < '2022-12-01'
    AND p.DURATION_TYPE = '30일 이상'
    and c.car_id NOT IN (
        SELECT car_id
        FROM car_rental_company_rental_history
        WHERE end_date >= "2022-11-01"
        AND start_date <= "2022-11-30")
    AND ROUND(c.DAILY_FEE * (1 - p.DISCOUNT_RATE / 100) * 30, 0) >= 500000
    AND ROUND(c.DAILY_FEE * (1 - p.DISCOUNT_RATE / 100) * 30, 0) < 2000000
ORDER BY 
    FEE DESC, c.CAR_TYPE, c.CAR_ID

-- not in 조건 쓰면 대여 한 적이 없는 자동차만 필터링 되기 때문에 확실하게 조회가능 한 것 같음. 
-- 음 날짜 조건 생각하는게 아직 많이 어려움(대여조건 같은 것)

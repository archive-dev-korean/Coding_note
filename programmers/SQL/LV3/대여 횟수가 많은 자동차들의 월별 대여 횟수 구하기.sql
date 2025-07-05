--문제 : CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: RECORDS) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 월을 기준으로 오름차순 정렬하고, 월이 같다면 자동차 ID를 기준으로 내림차순 정렬해주세요. 특정 월의 총 대여 횟수가 0인 경우에는 결과에서 제외해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/151139

--오답 쿼리1 : 
SELECT MONTH(START_DATE) as MONTH, CAR_ID, count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where START_DATE between '2022-08-01' and '2022-10-31' and (
select MONTH(START_DATE) as MONTH, count(*) 
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by MONTH(START_DATE)
having count(*) >= 5)
order by 1, 2 desc

--where절 문법적으로 잘못 사용함

--오답 쿼리2 : 
SELECT
    MONTH(START_DATE) AS MONTH,
    CAR_ID,
    COUNT(*) AS RECORDS
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE
    START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    AND MONTH(START_DATE) IN (
        SELECT MONTH(START_DATE)
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
        GROUP BY MONTH(START_DATE)
        HAVING COUNT(*) >= 5
    )
GROUP BY MONTH(START_DATE), CAR_ID
ORDER BY MONTH, CAR_ID DESC

--올바르게 사용했지만 조건에 부합하지는 않음

--정답 : 
SELECT MONTH(start_date) month, car_id, COUNT(*) records
FROM car_rental_company_rental_history
WHERE 
    start_date BETWEEN '2022-08-01' AND '2022-10-31' AND
    car_id IN (
        SELECT car_id
        FROM car_rental_company_rental_history
        WHERE start_date BETWEEN '2022-08-01' AND '2022-10-31' 
        GROUP BY car_id
        HAVING COUNT(*) >= 5)
GROUP BY MONTH(start_date), car_id
ORDER BY month ASC, car_id DESC
--간단하게 car_id 값으로 비교하면 구할수 있음...

--문제: CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 대여 시작일이 2022년 9월에 속하는 대여 기록에 대해서 대여 기간이 30일 이상이면 '장기 대여' 그렇지 않으면 '단기 대여' 로 표시하는 컬럼(컬럼명: RENT_TYPE)을 추가하여 대여기록을 출력하는 SQL문을 작성해주세요. 결과는 대여 기록 ID를 기준으로 내림차순 정렬해주세요.
--출처:  https://school.programmers.co.kr/learn/courses/30/lessons/151138

--Datediff 사용해서 대여 종료일과 시작을 차이를 계산 -> 29이상이면 장기대여 그외에는 단기대여로 처리
SELECT HISTORY_ID, CAR_ID, DATE_FORMAT(START_DATE,'%Y-%m-%d') AS START_DATE,DATE_FORMAT(END_DATE,'%Y-%m-%d') 
AS END_DATE, 
CASE WHEN DATEDIFF(END_DATE,START_DATE)>=29 THEN '장기 대여'
ELSE '단기 대여'
END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE START_DATE BETWEEN '2022-09-01' AND '2022-09-30'
ORDER BY HISTORY_ID DESC

--오답
SELECT HISTORY_ID,CAR_ID,DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE, DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
CASE 
WHEN END_DATE - START_DATE <30 THEN '단기대여' ELSE '장기대여' END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
where START_DATE like '2022-09%'
ORDER BY HISTORY_ID DESC
-- end_date - start_date가 연산이 되긴 하지만 다른 값이 나올 수 있음. 날짜 조건도 like보다는 between 사용하는 걸 권장

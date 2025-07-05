--문제 : CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 2022년 10월 16일에 대여 중인 자동차인 경우 '대여중' 이라고 표시하고, 대여 중이지 않은 자동차인 경우 '대여 가능'을 표시하는 컬럼(컬럼명: AVAILABILITY)을 추가하여 자동차 ID와 AVAILABILITY 리스트를 출력하는 SQL문을 작성해주세요. 이때 반납 날짜가 2022년 10월 16일인 경우에도 '대여중'으로 표시해주시고 결과는 자동차 ID를 기준으로 내림차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/157340

--오답 쿼리:
SELECT CAR_ID, 
       CASE 
            WHEN MAX_END_DATE >= '2022-10-16' THEN '대여중'
          ELSE '대여가능'
        END AS AVAILABILITY
FROM (
    SELECT CAR_ID, MAX(END_DATE) AS MAX_END_DATE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    GROUP BY CAR_ID
 ) AS sub
ORDER BY CAR_ID DESC;

--END_DATE만 비교해서 날짜 이상이면 대여중 아니면 대여가능 이라고 생각해서 이렇게 적었음 이렇게 적으면 모든 차량이 대여중으로 나옴

--정답 쿼리 : 
SELECT 
    CAR_ID,
    CASE 
        WHEN SUM(CASE WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE THEN 1 ELSE 0 END) > 0 
            THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY 
    CAR_ID
ORDER BY 
    CAR_ID DESC;

--이렇게 적는게 가독성도 그렇고 결과 해석하는데 좋은 것 같음. when sum()이 부분이 조금 헷갈리는데 
-- 이 차량의 모든 대여 기록 중에 10월 16일 기준 대여 중인 기록의 수를 세는 것이라고 보면 됨 <- 이부분 다시 한번 봐야 할듯
